from uuid import uuid4

from app.experts.compliance_expert import ComplianceExpert
from app.experts.document_expert import DocumentExpert
from app.experts.fraud_expert import FraudExpert
from app.experts.insurance_expert import InsuranceExpert
from app.experts.market_forecast_expert import MarketForecastExpert
from app.experts.personalization_expert import PersonalizationExpert
from app.experts.property_recommender import PropertyRecommenderExpert
from app.experts.residency_expert import ResidencyExpert
from app.experts.roi_expert import ROIExpert
from app.experts.valuation_expert import ValuationExpert
from app.schemas.ai import (
    AIAssessRequest,
    AIAssessResponse,
    AIResults,
    DecisionGovernance,
    ExpertAssessment,
    RankedRecommendation,
)
from app.services.base import AuditedService


class AIOrchestratorService(AuditedService):
    """Reference Mixture-of-Experts router for EstateOS decision workflows."""

    def __init__(self) -> None:
        self.property_recommender = PropertyRecommenderExpert()
        self.valuation_expert = ValuationExpert()
        self.roi_expert = ROIExpert()
        self.residency_expert = ResidencyExpert()
        self.insurance_expert = InsuranceExpert()
        self.fraud_expert = FraudExpert()
        self.compliance_expert = ComplianceExpert()
        self.document_expert = DocumentExpert()
        self.personalization_expert = PersonalizationExpert()
        self.market_forecast_expert = MarketForecastExpert()

    def assess(self, payload: AIAssessRequest) -> AIAssessResponse:
        request_id = f'ai-{uuid4()}'
        selected_experts = self._route(payload)
        self.audit('ai_request', request_id, 'routed', {'experts': selected_experts, 'intent': payload.intent})

        price = float(payload.input_payload.get('price', payload.input_payload.get('budget', 0)) or 0)
        uploaded_documents = int(payload.input_payload.get('uploaded_documents', 0) or 0)
        required_documents = int(payload.input_payload.get('required_documents', 0) or 0)
        transaction_stage = payload.context.transaction_stage or payload.input_payload.get('transaction_stage', 'intake')

        property_fit_score = self.property_recommender.score(payload)
        valuation_band = self.valuation_expert.estimate_band(price or 500000)
        estimated_yield = self.roi_expert.estimate_yield(payload)
        residency_result = self.residency_expert.assess(payload)
        compliance_risk = self.compliance_expert.risk(payload)
        insurance_relevance = self.insurance_expert.recommend(payload)
        fraud_status = self.fraud_expert.risk_flag(transaction_stage)
        document_completeness = self.document_expert.completeness(uploaded_documents, required_documents)
        personalization_profile = self.personalization_expert.segment(payload)
        market_outlook = self.market_forecast_expert.outlook(payload)

        expert_assessments = [
            ExpertAssessment(
                expert_key='property_recommender',
                score=property_fit_score,
                summary='Ranks inventory by cross-border fit, deal readiness, and livability.',
                rationale=[
                    'Considers budget, geography, and investor intent.',
                    'Elevates assets that remain financeable and residency-compatible.',
                ],
                confidence=0.88,
            ),
            ExpertAssessment(
                expert_key='valuation_expert',
                score=0.81,
                summary=f'Estimated fair-value band is {valuation_band}.',
                rationale=['Anchors price posture against a guarded valuation corridor.'],
                confidence=0.79,
            ),
            ExpertAssessment(
                expert_key='roi_expert',
                score=min(0.99, estimated_yield * 10),
                summary='Projects hold-period yield and downside resilience.',
                rationale=['Balances target returns with risk-tolerance input.'],
                confidence=0.76,
            ),
            ExpertAssessment(
                expert_key='residency_expert',
                score=0.85 if residency_result == 'preliminarily_eligible' else 0.58,
                summary=f'Residency workflow result: {residency_result}.',
                rationale=['Evaluates jurisdiction preference and migration goal.'],
                confidence=0.8,
            ),
            ExpertAssessment(
                expert_key='insurance_expert',
                score=0.77,
                summary='Suggests policy bundles and underwriting readiness.',
                rationale=['Maps product lines to transaction type and asset profile.'],
                confidence=0.74,
            ),
            ExpertAssessment(
                expert_key='fraud_expert',
                score=0.9 if fraud_status == 'clear' else 0.61,
                summary=f'Fraud review status is {fraud_status}.',
                rationale=['Escalates diligence-heavy stages for payment and identity review.'],
                confidence=0.82,
            ),
            ExpertAssessment(
                expert_key='compliance_expert',
                score=0.92 if compliance_risk == 'low' else 0.64,
                summary=f'Compliance risk is {compliance_risk}.',
                rationale=['Carries KYC, AML, sanctions, and privacy controls into release decisions.'],
                confidence=0.86,
            ),
            ExpertAssessment(
                expert_key='document_expert',
                score=document_completeness,
                summary='Measures document-pack completeness for underwriting and closing.',
                rationale=['Compares uploaded evidence against workflow requirements.'],
                confidence=0.72,
            ),
            ExpertAssessment(
                expert_key='personalization_expert',
                score=0.8,
                summary=f'Assigned user experience profile: {personalization_profile}.',
                rationale=['Keeps the frontend adaptive without bypassing trust controls.'],
                confidence=0.75,
            ),
            ExpertAssessment(
                expert_key='market_forecast_expert',
                score=0.78,
                summary=f'Market outlook: {market_outlook}.',
                rationale=['Adds jurisdiction-aware trend and policy-watch context.'],
                confidence=0.71,
            ),
        ]

        recommendations = [
            RankedRecommendation(
                candidate_id=payload.context.listing_id or 'listing-primary',
                title='Primary matched property',
                composite_score=round((property_fit_score + min(0.99, estimated_yield * 10) + document_completeness + 0.92) / 4, 2),
                reasons=[
                    'Balanced property fit, ROI, compliance, and documentation readiness.',
                    f'Insurance pathways: {", ".join(insurance_relevance)}.',
                ],
            ),
            RankedRecommendation(
                candidate_id='listing-secondary',
                title='Diversified backup option',
                composite_score=round(max(0.55, property_fit_score - 0.09), 2),
                reasons=[
                    'Maintains optionality if negotiation or compliance posture changes.',
                    'Suitable for advisor-led comparison and portfolio diversification.',
                ],
            ),
        ]

        trust_context = payload.trust_context
        human_review_required = bool(
            trust_context and (trust_context.human_review_required or trust_context.aml_risk in {'medium', 'high'} or trust_context.sanctions_status != 'clear')
        )
        policy_gates = [
            'Explainability packet attached',
            'Immutable audit event recorded',
            'Consent and privacy tier propagated',
            'KYC/AML/sanctions release gate evaluated',
        ]
        if document_completeness < 1:
            policy_gates.append('Document completion gate still open')
        if fraud_status != 'clear':
            policy_gates.append('Fraud review required before payment release')

        governance = DecisionGovernance(
            release_status='manual_review' if human_review_required or fraud_status != 'clear' or document_completeness < 1 else 'policy_cleared',
            review_queue='compliance_and_deal_desk' if human_review_required else 'straight_through_processing',
            policy_gates=policy_gates,
            audit_events=[
                'ai.request.routed',
                'ai.expert_assessments.completed',
                'ai.decision.release_evaluated',
            ],
        )
        self.audit('ai_request', request_id, 'assessed', governance.model_dump())

        return AIAssessResponse(
            request_id=request_id,
            selected_experts=selected_experts,
            results=AIResults(
                property_fit_score=property_fit_score,
                valuation_band=valuation_band,
                estimated_yield=estimated_yield,
                residency_result=residency_result,
                compliance_risk=compliance_risk,
                insurance_relevance=insurance_relevance,
                fraud_status=fraud_status,
                document_completeness=document_completeness,
                personalization_profile=personalization_profile,
                market_outlook=market_outlook,
                expert_assessments=expert_assessments,
                ranked_recommendations=recommendations,
            ),
            explanations=[
                'The orchestrator blended property, valuation, ROI, residency, insurance, fraud, compliance, document, personalization, and market experts.',
                'Release status remains explainable because every recommendation carries policy gates, audit events, and human-review conditions.',
            ],
            governance=governance,
        )

    def _route(self, payload: AIAssessRequest) -> list[str]:
        experts = ['property_recommender', 'valuation_expert', 'compliance_expert']
        if payload.intent in {'investment_property_with_residency', 'investment_analysis'}:
            experts.extend(['roi_expert', 'market_forecast_expert'])
        if payload.input_payload.get('requires_residency') or 'residency' in payload.intent:
            experts.append('residency_expert')
        if payload.input_payload.get('requires_insurance') or payload.input_payload.get('property_type'):
            experts.append('insurance_expert')
        if payload.context.transaction_stage or payload.input_payload.get('transaction_stage'):
            experts.extend(['fraud_expert', 'document_expert'])
        experts.append('personalization_expert')
        ordered = []
        for expert in experts:
            if expert not in ordered:
                ordered.append(expert)
        return ordered
