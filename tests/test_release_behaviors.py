"""发布门禁所需的关键兼容性回归测试。"""

from __future__ import annotations

import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
sys.path.insert(0, str(SCRIPTS))

from component_lint import lint_file  # noqa: E402
from minify_gzh_html import minify_html  # noqa: E402


class ComponentCompatibilityTests(unittest.TestCase):
    """验证公众号复制场景中的确定性布局规则。"""

    def lint_snippet(self, html: str):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "theme.md"
            path.write_text(f"```html\n{html}\n```\n", encoding="utf-8")
            return lint_file(str(path))[1]

    def test_half_width_component_is_rejected(self):
        findings = self.lint_snippet('<section style="width:50%;">内容</section>')
        self.assertTrue(any(level == "ERROR" and "50%" in message for level, message in findings))

    def test_full_width_component_is_allowed(self):
        findings = self.lint_snippet('<section style="width:100%;">内容</section>')
        self.assertEqual([], findings)


class CommandLineCompatibilityTests(unittest.TestCase):
    """验证公开命令行工具具备可发现的帮助入口。"""

    def test_public_scripts_support_help(self):
        scripts = (
            "component_lint.py",
            "minify_gzh_html.py",
            "upload_image.py",
            "wechat_draft.py",
            "wrap_preview.py",
        )
        for script in scripts:
            with self.subTest(script=script):
                result = subprocess.run(
                    [sys.executable, str(SCRIPTS / script), "--help"],
                    capture_output=True,
                    text=True,
                    encoding="utf-8",
                    errors="replace",
                    check=False,
                )
                self.assertEqual(0, result.returncode, result.stderr)
                self.assertIn("usage:", result.stdout.lower())

    def test_minifier_removes_source_whitespace(self):
        source = "<!-- 注释 --><section>\n  <p>正文</p>\n</section>"
        self.assertEqual("<section><p>正文</p></section>", minify_html(source))

    def test_core_validators_are_safe_on_gbk_console(self):
        """默认 GBK 控制台不能让校验脚本因装饰符号直接崩溃。"""
        env = dict(os.environ)
        env["PYTHONIOENCODING"] = "gbk"
        commands = (
            (
                "component_lint.py",
                str(ROOT),
            ),
            (
                "validate_gzh_html.py",
                str(ROOT / "docs" / "gallery" / "graphite-minimal.html"),
            ),
        )
        for script, argument in commands:
            with self.subTest(script=script):
                result = subprocess.run(
                    [sys.executable, str(SCRIPTS / script), argument],
                    capture_output=True,
                    text=True,
                    encoding="gbk",
                    errors="strict",
                    env=env,
                    check=False,
                )
                self.assertEqual(0, result.returncode, result.stderr)
                self.assertNotIn("UnicodeEncodeError", result.stderr)


if __name__ == "__main__":
    unittest.main()
