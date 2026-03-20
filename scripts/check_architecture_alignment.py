#!/usr/bin/env python3
"""Repository-level alignment check for the EstateOS MoE architecture.

This validator is intentionally lightweight. It does not claim that EstateOS has
fully implemented the target production platform; instead, it verifies that the
repository still preserves the requested blueprint through:

- canonical monorepo directory scaffolding,
- authoritative architecture documentation,
- documented service and expert boundaries, and
- reference implementation artifacts that reflect the expected control model.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]


@dataclass(frozen=True)
class CheckResult:
    name: str
    ok: bool
    detail: str


def read_text(relative_path: str) -> str:
    return (ROOT / relative_path).read_text(encoding="utf-8")


def require_path(relative_path: str, description: str) -> CheckResult:
    path = ROOT / relative_path
    return CheckResult(
        name=f"path:{relative_path}",
        ok=path.exists(),
        detail=description,
    )


def require_text(relative_path: str, required_snippets: list[str], description: str) -> CheckResult:
    path = ROOT / relative_path
    if not path.exists():
        return CheckResult(
            name=f"text:{relative_path}",
            ok=False,
            detail=f"{description} (missing file)",
        )

    contents = path.read_text(encoding="utf-8")
    missing = [snippet for snippet in required_snippets if snippet not in contents]
    if missing:
        return CheckResult(
            name=f"text:{relative_path}",
            ok=False,
            detail=f"{description} (missing snippets: {', '.join(missing)})",
        )

    return CheckResult(
        name=f"text:{relative_path}",
        ok=True,
        detail=description,
    )


def build_checks() -> list[CheckResult]:
    checks: list[CheckResult] = []

    for relative_path, description in [
        ("apps/web", "customer-facing Next.js app root exists"),
        ("apps/admin", "admin/broker/compliance app root exists"),
        ("apps/mobile", "optional mobile app root exists"),
        ("services/auth-service", "auth service boundary exists"),
        ("services/user-service", "user service boundary exists"),
        ("services/listing-service", "listing service boundary exists"),
        ("services/transaction-service", "transaction service boundary exists"),
        ("services/document-service", "document service boundary exists"),
        ("services/visa-service", "visa service boundary exists"),
        ("services/insurance-service", "insurance service boundary exists"),
        ("services/payment-service", "payment service boundary exists"),
        ("services/compliance-service", "compliance service boundary exists"),
        ("services/integration-service", "integration service boundary exists"),
        ("services/notification-service", "notification service boundary exists"),
        ("services/admin-reporting-service", "admin/reporting service boundary exists"),
        ("services/ai-orchestrator", "AI orchestrator service boundary exists"),
        ("experts/property-recommender", "property recommendation expert exists"),
        ("experts/valuation-expert", "valuation expert exists"),
        ("experts/roi-expert", "ROI expert exists"),
        ("experts/visa-expert", "visa expert exists"),
        ("experts/insurance-expert", "insurance expert exists"),
        ("experts/fraud-expert", "fraud expert exists"),
        ("experts/compliance-expert", "compliance expert exists"),
        ("experts/ux-expert", "UX expert exists"),
        ("experts/document-expert", "document intelligence expert exists"),
        ("experts/market-forecast-expert", "market forecast expert exists"),
        ("packages/ui", "shared UI package exists"),
        ("packages/types", "shared type package exists"),
        ("packages/config", "shared config package exists"),
        ("packages/shared-utils", "shared utility package exists"),
        ("infra/terraform", "Terraform infra root exists"),
        ("infra/bicep", "Bicep infra root exists"),
        ("infra/kubernetes", "Kubernetes infra root exists"),
    ]:
        checks.append(require_path(relative_path, description))

    checks.extend(
        [
            require_text(
                "README.md",
                [
                    "AI-native real estate operating system powered by a Mixture-of-Experts (MoE) backbone",
                    "Next.js + React + TypeScript",
                    "FastAPI (Python)",
                    "Azure Front Door",
                ],
                "root README preserves product framing, stack, and Azure baseline",
            ),
            require_text(
                "docs/authoritative-blueprint.md",
                [
                    "Property Recommendation Expert",
                    "Property Valuation Expert",
                    "Investment ROI Expert",
                    "Residency / Visa Eligibility Expert",
                    "Insurance Recommendation Expert",
                    "Payment / Fraud / Financial Risk Expert",
                    "Compliance / AML / Sanctions Expert",
                    "UX Personalization Expert",
                    "Document Intelligence Expert",
                    "Market Forecast / Trend Expert",
                    "API gateway",
                    "Backend-for-frontend (BFF)",
                ],
                "authoritative blueprint captures the canonical layered architecture and ten-expert taxonomy",
            ),
            require_text(
                "docs/blueprint-alignment.md",
                [
                    "`frontend/` remains prototype-only until the Next.js migration is complete",
                    "modular monolith first",
                    "orchestration entrypoints should converge under `services/ai-orchestrator/`",
                    "All infrastructure additions should preserve this Azure-native direction",
                ],
                "alignment guide encodes repository guardrails",
            ),
            require_text(
                "docs/compliance-mapping.md",
                [
                    "ISO/IEC 42001",
                    "ISO/IEC 5259",
                    "PCI DSS",
                    "SOC 2 Type 2",
                    "ACORD",
                    "NAIC",
                    "sanctions",
                    "PEP",
                ],
                "compliance mapping preserves the required governance posture",
            ),
            require_text(
                "services/ai-orchestrator/README.md",
                [
                    "intent detection",
                    "expert routing",
                    "explainability generation",
                    "policy and release gating",
                    "audit-packet assembly",
                ],
                "AI orchestrator service README preserves router responsibilities",
            ),
            require_text(
                "backend/orchestration.py",
                [
                    "capture identity, trust, and profile signals",
                    "route work to specialized experts",
                    "enforce policy gates",
                    "emit auditable event records",
                    "evaluate payment fraud, escrow conditions",
                    "continuously score compliance and operational risk",
                ],
                "reference orchestration implementation reflects the requested control model",
            ),
            require_text(
                "backend/api_contract.json",
                [
                    "Azure API Management",
                    "Azure Front Door",
                    "Azure Database for PostgreSQL",
                    "Azure Service Bus",
                    "Azure AI Search",
                    "Microsoft Entra External ID",
                    "IdentityTrustContext",
                    "DecisionRelease",
                ],
                "API contract preserves Azure-native and trust-context expectations",
            ),
        ]
    )

    return checks


def main() -> int:
    results = build_checks()

    print("EstateOS architecture alignment check")
    print("=" * 40)
    failed = False

    for result in results:
        marker = "PASS" if result.ok else "FAIL"
        print(f"[{marker}] {result.name} - {result.detail}")
        failed = failed or not result.ok

    print("=" * 40)
    if failed:
        print("Result: repository drift detected.")
        return 1

    print(
        "Result: repository remains aligned to the MoE blueprint as a governed "
        "scaffold/reference implementation."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
