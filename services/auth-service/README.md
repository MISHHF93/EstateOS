# Auth Service

`services/auth-service/` is the canonical home for EstateOS identity and trust-entry capabilities.

## Responsibilities

This service boundary should eventually own:

- authentication and session issuance,
- RBAC and fine-grained authorization primitives,
- MFA enrollment and enforcement,
- KYC initiation and status propagation,
- consent capture and consent-state lookup,
- access logging and trust-context publication.

## Architecture rules

- Keep identity, consent, and session controls explicit here rather than hiding them in UI code.
- Align with Keycloak or Microsoft Entra External ID / Azure AD B2C as the preferred identity baseline.
- Preserve auditability for sign-in, consent, privilege changes, and high-trust access decisions.
