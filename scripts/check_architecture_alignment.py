#!/usr/bin/env python3
"""Repository-level alignment check for the EstateOS MoE architecture.

This validator is intentionally lightweight. It does not claim that EstateOS has
fully implemented the target production platform; instead, it verifies that the
repository still preserves the requested blueprint through:

- canonical monorepo directory scaffolding,
- authoritative architecture documentation,
- documented service and expert boundaries,
- reference implementation artifacts that reflect the expected control model, and
- explicit current-state caveats so the repo does not over-claim production completeness.
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
                    "docs/current-state-alignment-audit.md",
                    "docs/blueprint-traceability-matrix.md",
                ],
                "root README preserves product framing, stack, Azure baseline, and current-state audit references",
            ),
            require_text(
                "docs/authoritative-blueprint.md",
                [
                    "Backend-for-frontend (BFF)",
                    "Property search and maps.",
                    "Documents / eSignature / deal room.",
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
                    "international investor",
                    "first-time renter",
                    "Mapbox or Google Maps",
                    "Stripe Elements or payment SDKs where relevant.",
                    "Azure Front Door",
                    "Azure Machine Learning",
                    "ISO/IEC 42001",
                    "ISO/IEC 5259",
                ],
                "authoritative blueprint captures the layered architecture, ten-expert taxonomy, routing examples, stack decisions, Azure layout, and AI-governance controls",
            ),
            require_text(
                "docs/architecture.md",
                [
                    "investor dashboard",
                    "payments / escrow UI",
                    "documents / eSignature / deal room",
                    "rate limiting",
                    "consent hooks",
                    "audit hooks",
                    "feature store / ML data layer",
                    "SOC 2 Type 2",
                ],
                "architecture doc preserves the requested layered UX, control-plane, data-platform, and governance requirements",
            ),
            require_text(
                "docs/platform-manifest.md",
                [
                    "property discovery and maps",
                    "broker / admin / compliance operations",
                    "policy and human-review gating",
                    "data quality, lineage, and auditability",
                    "payment flows should remain PCI-aware and tokenized",
                ],
                "platform manifest preserves operational guardrails for UX, orchestration, data governance, and payment/compliance controls",
            ),
            require_text(
                "docs/blueprint-alignment.md",
                [
                    "`frontend/` remains prototype-only until the Next.js migration is complete",
                    "modular monolith first",
                    "orchestration entrypoints should converge under `services/ai-orchestrator/`",
                    "All infrastructure additions should preserve this Azure-native direction",
                    "trust, audit, privacy, and compliance implications",
                ],
                "alignment guide encodes repository guardrails and contributor obligations",
            ),
            require_text(
                "docs/compliance-mapping.md",
                [
                    "ISO/IEC 42001",
                    "ISO/IEC 5259",
                    "ISO 9241-210",
                    "PCI DSS",
                    "SOC 2 Type 2",
                    "ACORD",
                    "NAIC",
                    "sanctions",
                    "PEP",
                    "beneficial ownership",
                    "incident response",
                ],
                "compliance mapping preserves the required governance posture",
            ),
            require_text(
                "docs/blueprint-traceability-matrix.md",
                [
                    "Frontend experience layer",
                    "API gateway / BFF layer",
                    "International investor and first-time renter routing examples",
                    "Service Bus/Event Grid",
                    "Phase 2 and Phase 3 capabilities are preserved as explicit future scope",
                    "not yet the final fully implemented production platform",
                ],
                "traceability matrix ties each major blueprint requirement to concrete repository evidence and current-state caveats",
            ),
            require_text(
                "docs/current-state-alignment-audit.md",
                [
                    "yes at the repository-governance and reference-implementation level",
                    "frontend/` as a prototype rather than a production `apps/web/` Next.js app",
                    "BFF/API layer is documented rather than materialized",
                    "governed scaffold",
                ],
                "current-state audit truthfully distinguishes architectural alignment from full production completeness",
            ),
            require_text(
                "docs/architecture-scorecard.md",
                [
                    "Aligned as scaffold",
                    "Aligned as architectural rule",
                    "Aligned as governance baseline",
                    "Does it avoid overstating current implementation maturity relative to the roadmap phase actually delivered?",
                ],
                "architecture scorecard preserves the layer-by-layer verdict and anti-overclaim guardrail",
            ),
            require_text(
                "apps/web/README.md",
                [
                    "public marketing pages",
                    "property discovery and maps",
                    "investor workspace",
                    "residency / visa intake",
                    "insurance flows",
                    "payments / escrow UI",
                    "documents / eSignature / deal-room workflows",
                    "AI insights, recommendations, and risk explanations",
                    "Next.js App Router",
                    "Stripe Elements or equivalent payment SDKs",
                ],
                "web app README preserves the required frontend zones and locked stack guidance",
            ),
            require_text(
                "apps/admin/README.md",
                [
                    "brokers, administrators, compliance reviewers, and support teams",
                    "KYC / AML / sanctions oversight",
                    "payment / escrow monitoring",
                    "explainability and release-gating visibility",
                ],
                "admin app README preserves the operator/compliance console remit",
            ),
            require_text(
                "services/ai-orchestrator/README.md",
                [
                    "intent detection",
                    "expert routing",
                    "explainability generation",
                    "policy and release gating",
                    "audit-packet assembly",
                    "human-review escalation hooks",
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
                    "validate, transform, and route partner API payloads",
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
