"""Internal module：提供在 Windows 中文控制台下不会因符号编码而崩溃的输出函数。"""

from __future__ import annotations

import sys
from typing import Optional, TextIO


SCRIPT_INTERFACE = "internal-module"


# 这些符号在 UTF-8 终端里可读，但在默认 GBK 控制台里经常无法编码。
_CONSOLE_REPLACEMENTS = (
    ("⚠️", "[WARN]"),
    ("📋", "[INFO]"),
    ("📐", "[INFO]"),
    ("❌", "[ERROR]"),
    ("✗", "[ERROR]"),
    ("✅", "[OK]"),
    ("✓", "[OK]"),
    ("→", "->"),
    ("•", "-"),
    ("──", "--"),
    ("—", "-"),
    ("…", "..."),
    ("·", "-"),
    ("≤", "<="),
)


def _safe_text(value: object, encoding: str) -> str:
    """将终端不支持的装饰符号降级，保留中文诊断信息。"""
    text = str(value)
    for source, replacement in _CONSOLE_REPLACEMENTS:
        text = text.replace(source, replacement)
    try:
        text.encode(encoding)
    except UnicodeEncodeError:
        # 用户输入或文件名仍可能带有终端不支持的字符；只替换无法显示的
        # 字符，避免诊断流程因输出失败而掩盖真正的校验结果。
        text = text.encode(encoding, errors="replace").decode(encoding)
    return text


def safe_print(
    *values: object,
    sep: str = " ",
    end: str = "\n",
    file: Optional[TextIO] = None,
    flush: bool = False,
) -> None:
    """安全输出中文诊断信息，不让控制台编码异常中断脚本。"""
    stream = file or sys.stdout
    encoding = getattr(stream, "encoding", None) or "utf-8"
    rendered = sep.join(_safe_text(value, encoding) for value in values)
    stream.write(rendered + _safe_text(end, encoding))
    if flush:
        stream.flush()
