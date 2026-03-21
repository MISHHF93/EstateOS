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


orchestration = load_module("orchestration_payloads", "backend/orchestration.py")


class OrchestrationPayloadTests(unittest.TestCase):
    def test_build_demo_payloads_includes_compliance_graph_packet(self):
        payload = orchestration.build_demo_payloads("buyer")

        self.assertIn("compliance_graph_decision", payload)
        packet = payload["compliance_graph_decision"]
        self.assertEqual(packet["primary_jurisdiction"], "Portugal")
        self.assertIn("real_estate", {item["domain"] for item in packet["domains"]})
        self.assertIn("payments", {item["domain"] for item in packet["domains"]})
        self.assertGreaterEqual(len(packet["workflow_adaptations"]), 4)
        self.assertGreaterEqual(len(packet["change_watch"]), 4)

    def test_compliance_graph_mentions_cross_domain_statuses(self):
        payload = orchestration.build_demo_payloads("investor")
        packet = payload["compliance_graph_decision"]

        self.assertIn("payment risk", packet["graph_summary"])
        self.assertIn("residency", packet["graph_summary"])
        self.assertIn(packet["overall_status"], {"active", "review"})


if __name__ == "__main__":
    unittest.main()
