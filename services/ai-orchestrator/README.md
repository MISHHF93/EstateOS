# AI Orchestrator Service

`services/ai-orchestrator/` is the canonical backend home for the EstateOS expert router and orchestration logic.

## Responsibilities

This service should eventually own:

- intent detection,
- profile and trust-context assembly,
- expert routing,
- expert result aggregation and ranking,
- explainability generation,
- policy and release gating,
- audit-packet assembly,
- human-review escalation hooks.

## Alignment rules

The orchestrator should stay consistent with the ten-expert MoE model documented in `docs/moe-platform-model.md`.

The current `backend/orchestration.py` file is a reference blueprint only. Production-oriented orchestration work should converge here instead.
