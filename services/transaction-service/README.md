# Transaction Service

`services/transaction-service/` owns EstateOS deal execution from reservation through milestone completion.

## Responsibilities

This service boundary should eventually own:

- offers and reservations,
- transaction-stage state machines,
- milestone tracking,
- deal-room handoffs,
- workflow events for documents, payments, and notifications,
- auditable lifecycle transitions.

## Architecture rules

- Preserve sequential, replayable state transitions for every transaction.
- Keep payment, document, compliance, and notification integrations explicit rather than embedding them in UI logic.
- Design for workflow-orchestrator compatibility with Temporal or Camunda.
