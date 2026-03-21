from dataclasses import dataclass


@dataclass(frozen=True)
class DeferredTask:
    name: str
    queue: str
    description: str


TASK_CATALOG = [
    DeferredTask(name='document-extraction', queue='documents', description='Run OCR, classification, and legal-entity extraction for uploaded deal and residency evidence.'),
    DeferredTask(name='listing-index', queue='search', description='Project listing and property updates into Azure AI Search with personalization facets.'),
    DeferredTask(name='residency-assessment', queue='workflow', description='Run asynchronous residency eligibility scoring and document sufficiency checks.'),
    DeferredTask(name='insurance-marketplace-fanout', queue='insurance', description='Dispatch ACORD-aligned quote requests to approved carriers and aggregators.'),
    DeferredTask(name='payment-reconciliation', queue='payments', description='Reconcile PSP callbacks, escrow events, and fraud review outcomes.'),
    DeferredTask(name='compliance-screening', queue='compliance', description='Trigger KYC, AML, sanctions, PEP, and beneficial ownership monitoring workflows.'),
    DeferredTask(name='market-signal-refresh', queue='ai', description='Refresh market forecasts, pricing signals, and feature-store snapshots for MoE experts.'),
    DeferredTask(name='notification-dispatch', queue='notifications', description='Route omnichannel notifications and regulator-mandated alerts through governed templates.'),
    DeferredTask(name='integration-webhook-processing', queue='integrations', description='Normalize partner callbacks, validate signatures, and emit canonical events.'),
    DeferredTask(name='ledger-closeout', queue='payments', description='Finalize escrow, reconciliation, and immutable ledger closeout packets.'),
]
