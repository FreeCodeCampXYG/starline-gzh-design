#!/usr/bin/env python3
"""Validate and apply small, reversible block-level AI edit operations."""
from __future__ import annotations

import argparse
import copy
import json
import sys
from pathlib import Path


def fail(message: str) -> None:
    raise ValueError(message)


def validate_operation(document: dict, operation: dict) -> None:
    blocks = {block.get("id"): block for block in document.get("blocks", [])}
    target_ids = operation.get("target_ids") or []
    if not operation.get("op_id") or not operation.get("kind"):
        fail("operation requires op_id and kind")
    if operation.get("status") not in {"pending", "accepted", "rejected"}:
        fail("operation status must be pending, accepted, or rejected")
    if not target_ids or any(target_id not in blocks for target_id in target_ids):
        fail("operation target_ids must reference existing blocks")
    if operation.get("status") == "accepted":
        before = operation.get("before")
        after = operation.get("after")
        if not isinstance(before, dict) or not isinstance(after, dict):
            fail("accepted operation requires before and after objects")
        for target_id in target_ids:
            if before.get(target_id, {}).get("text") != blocks[target_id].get("text"):
                fail(f"before text does not match current block: {target_id}")
        if not isinstance(operation.get("inverse_patch"), dict):
            fail("accepted operation requires inverse_patch")


def apply_operation(document: dict, operation: dict) -> dict:
    result = copy.deepcopy(document)
    validate_operation(result, operation)
    if operation["status"] != "accepted":
        return result
    blocks = {block["id"]: block for block in result["blocks"]}
    for target_id in operation["target_ids"]:
        replacement = operation["after"].get(target_id)
        if not isinstance(replacement, dict) or "text" not in replacement:
            fail(f"after text missing for block: {target_id}")
        blocks[target_id]["text"] = replacement["text"]
    result["source_version"] = int(result.get("source_version", 0)) + 1
    result.setdefault("operations", []).append(copy.deepcopy(operation))
    return result


def undo_operation(document: dict, operation: dict) -> dict:
    result = copy.deepcopy(document)
    if operation.get("status") != "accepted":
        fail("only accepted operations can be undone")
    inverse = operation.get("inverse_patch") or {}
    blocks = {block["id"]: block for block in result.get("blocks", [])}
    for target_id in operation.get("target_ids", []):
        if target_id not in blocks or target_id not in inverse:
            fail(f"inverse patch missing for block: {target_id}")
        blocks[target_id]["text"] = inverse[target_id]["text"]
    result["source_version"] = int(result.get("source_version", 0)) + 1
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("document", type=Path)
    parser.add_argument("operation", type=Path)
    parser.add_argument("--undo", action="store_true")
    args = parser.parse_args()
    try:
        document = json.loads(args.document.read_text(encoding="utf-8"))
        operation = json.loads(args.operation.read_text(encoding="utf-8"))
        output = undo_operation(document, operation) if args.undo else apply_operation(document, operation)
        json.dump(output, sys.stdout, ensure_ascii=False, indent=2)
        sys.stdout.write("\n")
        return 0
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
