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
- human-review escalation hooks,
- event publication for AI lifecycle updates,
- Azure Machine Learning and Azure AI Search integration seams.

## Canonical expert mesh

The orchestrator should remain consistent with the ten-expert MoE model documented in `docs/moe-platform-model.md`:

1. property recommendation,
2. valuation,
3. ROI analysis,
4. residency eligibility,
5. insurance matching,
6. fraud detection,
7. compliance / AML / sanctions,
8. document intelligence,
9. personalization,
10. market forecasting.

## Output contract

Production routing should return:

- selected experts,
- per-expert assessments,
- ranked recommendations,
- explainable rationale,
- policy gates,
- release status,
- audit references.

The current `backend/orchestration.py` file is a reference blueprint only. Production-oriented orchestration work should converge here instead.
