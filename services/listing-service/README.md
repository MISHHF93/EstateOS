# Listing Service

`services/listing-service/` is the canonical home for the EstateOS property catalog and discovery domain.

## Responsibilities

This service boundary should eventually own:

- property catalog ingestion and lifecycle,
- search/filter contracts,
- listing media metadata,
- map-facing discovery payloads,
- listing quality/moderation workflows,
- availability and merchandising signals consumed by recommendation logic.

## Architecture rules

- Preserve clean boundaries between listing facts, ranking logic, and UI presentation.
- Keep search/index assumptions explicit so PostgreSQL and Azure AI Search/Elasticsearch can evolve cleanly.
- Expose stable contracts for discovery, investor, insurance, and transaction flows.
