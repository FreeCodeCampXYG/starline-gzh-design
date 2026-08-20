import tempfile
import unittest
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
VALIDATOR = ROOT / "scripts" / "validate_gzh_html.py"


class MediaContractTests(unittest.TestCase):
    def run_validator(self, html):
        with tempfile.NamedTemporaryFile("w", suffix=".html", encoding="utf-8", delete=False) as handle:
            handle.write(html)
            path = handle.name
        return subprocess.run([sys.executable, str(VALIDATOR), path], capture_output=True, text=True, encoding="utf-8", errors="replace")

    def test_svg_is_rejected(self):
        result = self.run_validator('<section><svg><text><span leaf="">图</span></text></svg></section>')
        self.assertNotEqual(result.returncode, 0)

    def test_javascript_url_is_rejected(self):
        result = self.run_validator('<section><img src="javascript:alert(1)" /></section>')
        self.assertNotEqual(result.returncode, 0)


if __name__ == "__main__":
    unittest.main()
