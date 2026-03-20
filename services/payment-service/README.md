# Payment Service

`services/payment-service/` owns EstateOS payment, ledger, reconciliation, and escrow-style workflow coordination.

## Responsibilities

This service boundary should eventually own:

- payment-intent orchestration,
- PSP integration and tokenized payment references,
- ledger and reconciliation records,
- escrow-style workflow checkpoints,
- refund/disbursement coordination,
- fraud-hook invocation and payment-event evidence.

## Architecture rules

- Keep cardholder data out of the platform wherever possible by using hosted/tokenized PSP flows.
- Preserve PCI-aware boundaries, settlement traceability, and immutable reconciliation evidence.
- Integrate tightly with fraud, compliance, and transaction-stage controls before release of funds or irreversible actions.
