import pathlib
import unittest


ROOT = pathlib.Path(__file__).resolve().parents[1]


class PlatformBlueprintContractTests(unittest.TestCase):
    def test_production_blueprint_captures_required_platform_elements(self):
        content = (ROOT / 'docs/production-platform-blueprint.md').read_text(encoding='utf-8')
        required_snippets = [
            'Next.js + React + TypeScript',
            'Python FastAPI',
            'Azure API Management',
            'Azure Machine Learning',
            'Relational schema baseline',
            'ai.request.routed',
            'ISO/IEC 42001',
            'ISO/IEC 5259',
            'ACORD-oriented insurance interoperability',
            'beneficial ownership controls',
        ]
        for snippet in required_snippets:
            with self.subTest(snippet=snippet):
                self.assertIn(snippet, content)

    def test_entity_model_covers_core_operating_system_records(self):
        content = (ROOT / 'backend/app/models/entities.py').read_text(encoding='utf-8')
        for entity_name in [
            'class Role',
            'class UserProfile',
            'class Property',
            'class DealParticipant',
            'class ResidencyApplication',
            'class InsuranceRequest',
            'class PaymentIntent',
            'class ComplianceCase',
            'class AIRequest',
        ]:
            with self.subTest(entity_name=entity_name):
                self.assertIn(entity_name, content)

    def test_event_contracts_cover_key_lifecycle_packets(self):
        content = (ROOT / 'backend/app/events/contracts.py').read_text(encoding='utf-8')
        for event_name in [
            'LISTING_PUBLISHED',
            'DEAL_CREATED',
            'DOCUMENT_UPLOADED',
            'AI_REQUEST_ROUTED',
            'PAYMENT_SUCCEEDED',
            'RESIDENCY_ASSESSMENT_COMPLETED',
            'INSURANCE_QUOTE_REQUESTED',
            'COMPLIANCE_CASE_ESCALATED',
        ]:
            with self.subTest(event_name=event_name):
                self.assertIn(event_name, content)


if __name__ == '__main__':
    unittest.main()
