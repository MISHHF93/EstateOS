# Shared Config

`packages/config/` is reserved for reusable configuration contracts and policy-oriented defaults.

## Expected contents

This package should eventually centralize:

- environment configuration schemas,
- feature-flag definitions,
- routing and release-policy defaults,
- audit/logging config primitives,
- service-to-service configuration contracts,
- deployment-time validation helpers.

## Architecture rule

Keep configuration typed, reviewable, and reusable so service and app boundaries do not drift through ad hoc environment variables.
