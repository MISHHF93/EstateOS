import importlib.util
import sys
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


def load_module(name: str, relative_path: str):
    module_path = REPO_ROOT / relative_path
    spec = importlib.util.spec_from_file_location(name, module_path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


wiring = load_module("check_frontend_wiring", "scripts/check_frontend_wiring.py")


class CheckFrontendWiringTests(unittest.TestCase):
    def test_assert_condition_raises_wiring_error(self):
        with self.assertRaises(wiring.WiringError):
            wiring.assert_condition(False, "broken")

    def test_validate_packets_accepts_complete_packet_set(self):
        packets = {key: {"status": "ok"} for key in wiring.REQUIRED_DECISION_KEYS}
        wiring.validate_packets("buyer", packets)

    def test_validate_packets_rejects_missing_required_keys(self):
        packets = {key: {"status": "ok"} for key in wiring.REQUIRED_DECISION_KEYS}
        packets.pop("payment_decision")

        with self.assertRaises(wiring.WiringError) as context:
            wiring.validate_packets("buyer", packets)

        self.assertIn("payment_decision", str(context.exception))

    def test_get_free_port_returns_bindable_port(self):
        port = wiring.get_free_port()
        self.assertIsInstance(port, int)
        self.assertGreater(port, 0)


if __name__ == "__main__":
    unittest.main()
