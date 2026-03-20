import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock


REPO_ROOT = Path(__file__).resolve().parents[1]


def load_module(name: str, relative_path: str):
    module_path = REPO_ROOT / relative_path
    spec = importlib.util.spec_from_file_location(name, module_path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


alignment = load_module("check_architecture_alignment", "scripts/check_architecture_alignment.py")


class CheckArchitectureAlignmentTests(unittest.TestCase):
    def test_require_text_reports_missing_snippets(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            target = root / "README.md"
            target.write_text("alpha beta gamma", encoding="utf-8")

            with mock.patch.object(alignment, "ROOT", root):
                result = alignment.require_text(
                    "README.md",
                    ["alpha", "delta"],
                    "doc keeps required content",
                )

        self.assertFalse(result.ok)
        self.assertIn("delta", result.detail)

    def test_require_json_accepts_valid_json(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            target = root / "config.json"
            target.write_text(json.dumps({"ok": True}), encoding="utf-8")

            with mock.patch.object(alignment, "ROOT", root):
                result = alignment.require_json("config.json", "json is valid")

        self.assertTrue(result.ok)
        self.assertEqual(result.detail, "json is valid")

    def test_require_command_captures_nonzero_exit(self):
        result = alignment.require_command(
            ["python3", "-c", "import sys; sys.exit(3)"],
            "command should succeed",
        )

        self.assertFalse(result.ok)
        self.assertIn("exit 3", result.detail)

    def test_main_returns_zero_when_all_results_pass(self):
        fake_results = [alignment.CheckResult(name="ok", ok=True, detail="all good")]

        with mock.patch.object(alignment, "build_checks", return_value=fake_results):
            exit_code = alignment.main()

        self.assertEqual(exit_code, 0)


if __name__ == "__main__":
    unittest.main()
