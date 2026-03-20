# Shared Types

`packages/types/` is reserved for cross-cutting platform contracts used across apps, services, experts, and infrastructure.

## Expected contents

This package should eventually define shared schemas for:

- identities and sessions,
- user and investor profiles,
- listings and search payloads,
- transaction and milestone events,
- payments, ledgers, and escrow state,
- compliance decisions and audit packets,
- expert routing inputs/outputs,
- AI explanations and confidence metadata.

## Architecture rule

If a schema is reused by more than one app or service boundary, it should usually be defined here rather than copied into feature-local code.
