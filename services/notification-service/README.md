# Notification Service

`services/notification-service/` owns EstateOS cross-channel messaging and user-journey communication flows.

## Responsibilities

This service boundary should eventually own:

- email, SMS, and push delivery orchestration,
- transactional notification templates,
- preference-aware routing,
- milestone and exception messaging,
- reminder/escalation workflows,
- delivery evidence and retry handling.

## Architecture rules

- Keep communication policies centralized so product surfaces do not fork message behavior.
- Respect consent, privacy, locale, and notification-preference constraints.
- Preserve operational evidence for critical alerts tied to transactions, compliance, and payments.
