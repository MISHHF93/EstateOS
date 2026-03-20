# Integration Service

`services/integration-service/` owns partner API adapters, webhook processing, and external-system integration patterns.

## Responsibilities

This service boundary should eventually own:

- broker/partner API adapters,
- insurer and PSP integration connectors,
- government or residency-system integration points,
- inbound/outbound webhooks,
- retry, idempotency, and dead-letter handling for external calls,
- contract translation between internal and third-party schemas.

## Architecture rules

- Keep vendor-specific integration logic isolated from core domain services.
- Publish stable internal contracts so partners can change without cascading architecture drift.
- Preserve observability, replay safety, and evidence capture for every external exchange.
