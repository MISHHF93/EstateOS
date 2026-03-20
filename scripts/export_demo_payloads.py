#!/usr/bin/env python3
"""Export stable demo packets from the orchestration reference implementation."""

from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
import json
import sys


ROOT = Path(__file__).resolve().parents[1]
OUTPUT_PATH = ROOT / "frontend" / "demo-packets.json"
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from backend.orchestration import build_demo_payloads

IDENTIFIER_OVERRIDES = {
    "request_id": "demo-request",
    "transaction_id": "demo-transaction",
    "transaction_reference": "demo-transaction",
    "subject_id": "demo-subject",
    "applicant_id": "demo-applicant",
    "payer_id": "demo-payer",
}


def normalize(value):
    if isinstance(value, dict):
        normalized = {}
        for key, item in value.items():
            if key in IDENTIFIER_OVERRIDES:
                normalized[key] = IDENTIFIER_OVERRIDES[key]
            elif key.endswith("_utc"):
                normalized[key] = "2026-03-20T00:00:00+00:00"
            else:
                normalized[key] = normalize(item)
        return normalized
    if isinstance(value, list):
        return [normalize(item) for item in value]
    return value


def main() -> None:
    payload = {
        "meta": {
            "generated_at_utc": datetime.now(timezone.utc).isoformat(),
            "generated_from": "backend.orchestration.build_demo_payloads",
            "normalized": True,
        },
        "packets": normalize(build_demo_payloads()),
    }
    OUTPUT_PATH.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(f"Exported demo packets to {OUTPUT_PATH.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
