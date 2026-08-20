import json
import tempfile
import unittest
from pathlib import Path
import importlib.util

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("edit_contract", ROOT / "scripts" / "edit_contract.py")
edit_contract = importlib.util.module_from_spec(spec)
spec.loader.exec_module(edit_contract)


class EditContractTests(unittest.TestCase):
    def setUp(self):
        self.document = {
            "source_version": 0,
            "blocks": [
                {"id": "p-1", "type": "paragraph", "text": "原文一"},
                {"id": "p-2", "type": "paragraph", "text": "原文二"},
            ],
        }
        self.operation = {
            "op_id": "op-1",
            "kind": "rewrite",
            "target_ids": ["p-1"],
            "before": {"p-1": {"text": "原文一"}},
            "after": {"p-1": {"text": "改写一"}},
            "inverse_patch": {"p-1": {"text": "原文一"}},
            "status": "accepted",
        }

    def test_non_target_block_is_unchanged(self):
        result = edit_contract.apply_operation(self.document, self.operation)
        self.assertEqual(result["blocks"][1]["text"], "原文二")
        self.assertEqual(result["blocks"][0]["text"], "改写一")

    def test_undo_restores_exact_text(self):
        result = edit_contract.apply_operation(self.document, self.operation)
        undone = edit_contract.undo_operation(result, self.operation)
        self.assertEqual(undone["blocks"][0]["text"], "原文一")

    def test_rejected_is_noop(self):
        rejected = dict(self.operation, status="rejected")
        result = edit_contract.apply_operation(self.document, rejected)
        self.assertEqual(result, self.document)

    def test_before_mismatch_fails(self):
        mismatched = dict(self.operation, before={"p-1": {"text": "错误"}})
        with self.assertRaises(ValueError):
            edit_contract.apply_operation(self.document, mismatched)


if __name__ == "__main__":
    unittest.main()
