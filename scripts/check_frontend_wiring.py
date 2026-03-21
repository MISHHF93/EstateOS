#!/usr/bin/env python3
"""Smoke-test the served frontend wiring against the generated demo snapshot.

This check intentionally stays dependency-light. It serves the static prototype from
`frontend/`, fetches the exact asset paths the browser would request, and validates
that the HTML, JavaScript, and JSON snapshot still agree on the packet contract.
"""

from __future__ import annotations

from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.request import urlopen
import contextlib
import json
import socket
import threading


ROOT = Path(__file__).resolve().parents[1]
FRONTEND_ROOT = ROOT / "frontend"
REQUIRED_DECISION_KEYS = {
    "journey_key",
    "property_decision",
    "transaction_decision",
    "payment_decision",
    "insurance_decision",
    "integration_decision",
    "residency_decision",
    "compliance_graph_decision",
    "digital_twin_decision",
    "market_intelligence_decision",
    "document_intelligence_decision",
    "tokenization_decision",
    "copilot_decision",
}
REQUIRED_JOURNEYS = {"buyer", "investor", "advisor"}


class WiringError(RuntimeError):
    """Raised when the prototype wiring contract is broken."""


def get_free_port() -> int:
    with contextlib.closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as sock:
        sock.bind(("127.0.0.1", 0))
        sock.listen(1)
        return int(sock.getsockname()[1])


def fetch_text(url: str) -> str:
    with urlopen(url) as response:  # noqa: S310 - local ephemeral HTTP server only
        return response.read().decode("utf-8")


def fetch_json(url: str) -> dict:
    with urlopen(url) as response:  # noqa: S310 - local ephemeral HTTP server only
        return json.loads(response.read().decode("utf-8"))


def assert_condition(condition: bool, message: str) -> None:
    if not condition:
        raise WiringError(message)


def validate_packets(name: str, packets: dict) -> None:
    missing = sorted(REQUIRED_DECISION_KEYS - set(packets))
    assert_condition(not missing, f"{name} missing packet keys: {', '.join(missing)}")


def main() -> None:
    handler = partial(SimpleHTTPRequestHandler, directory=str(FRONTEND_ROOT))
    port = get_free_port()
    server = ThreadingHTTPServer(("127.0.0.1", port), handler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()

    try:
        base_url = f"http://127.0.0.1:{port}"
        html = fetch_text(f"{base_url}/")
        app_js = fetch_text(f"{base_url}/app.js")
        styles = fetch_text(f"{base_url}/styles.css")
        snapshot = fetch_json(f"{base_url}/demo-packets.json")

        assert_condition('<link rel="stylesheet" href="styles.css"' in html, "index.html no longer links to styles.css")
        assert_condition('src="app.js"' in html, "index.html no longer loads app.js")
        assert_condition('id="wiring-title"' in html, "index.html is missing the system wiring banner")
        assert_condition('./demo-packets.json' in app_js, "frontend app no longer fetches demo-packets.json")
        assert_condition('journeys?.[state.activeJourney]?.packets' in app_js, "frontend app no longer reads journey-scoped packets")
        assert_condition('backendSnapshot.data?.packets' in app_js, "frontend app no longer supports top-level packet fallback")
        assert_condition('.wiring-banner' in styles or '#wiring-title' in styles or '.wiring-card' in styles, "styles.css is missing wiring-banner styling hooks")

        assert_condition(snapshot.get('meta', {}).get('generated_from') == 'backend.orchestration.build_demo_payloads', "demo snapshot was not generated from backend.orchestration.build_demo_payloads")

        journeys = snapshot.get('journeys', {})
        assert_condition(REQUIRED_JOURNEYS.issubset(journeys), f"demo snapshot missing journeys: {', '.join(sorted(REQUIRED_JOURNEYS - set(journeys)))}")

        for journey_name in sorted(REQUIRED_JOURNEYS):
            journey_payload = journeys[journey_name]
            packets = journey_payload.get('packets')
            assert_condition(isinstance(packets, dict), f"journey '{journey_name}' is missing a packets object")
            validate_packets(f"journey '{journey_name}'", packets)

        top_level_packets = snapshot.get('packets')
        assert_condition(isinstance(top_level_packets, dict), "demo snapshot is missing the top-level packets object")
        validate_packets('top-level packets', top_level_packets)

        print('Frontend wiring smoke test passed')
        print(f'Served frontend root: {base_url}/')
        print(f'Journeys validated: {", ".join(sorted(REQUIRED_JOURNEYS))}')
    finally:
        server.shutdown()
        server.server_close()
        thread.join(timeout=1)


if __name__ == '__main__':
    main()
