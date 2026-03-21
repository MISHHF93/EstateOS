import pathlib
import unittest


ROOT = pathlib.Path(__file__).resolve().parents[1]


class FastAPIScaffoldTests(unittest.TestCase):
    def test_expected_backend_files_exist(self):
        expected = [
            ROOT / 'backend/app/main.py',
            ROOT / 'backend/app/api/router.py',
            ROOT / 'backend/app/services/ai_orchestrator.py',
            ROOT / 'backend/app/events/contracts.py',
            ROOT / 'backend/app/workers/tasks.py',
            ROOT / 'backend/app/experts/personalization_expert.py',
            ROOT / 'backend/app/experts/market_forecast_expert.py',
            ROOT / 'backend/pyproject.toml',
        ]
        for path in expected:
            with self.subTest(path=path):
                self.assertTrue(path.exists(), f'Missing scaffold file: {path}')

    def test_main_registers_api_versioned_router(self):
        content = (ROOT / 'backend/app/main.py').read_text(encoding='utf-8')
        self.assertIn("application.include_router(api_router, prefix=settings.api_prefix)", content)
        self.assertIn("/health", content)

    def test_ai_orchestrator_routes_broad_expert_mesh(self):
        content = (ROOT / 'backend/app/services/ai_orchestrator.py').read_text(encoding='utf-8')
        self.assertIn('investment_property_with_residency', content)
        self.assertIn('property_recommender', content)
        self.assertIn('valuation_expert', content)
        self.assertIn('roi_expert', content)
        self.assertIn('residency_expert', content)
        self.assertIn('insurance_expert', content)
        self.assertIn('fraud_expert', content)
        self.assertIn('document_expert', content)
        self.assertIn('personalization_expert', content)
        self.assertIn('market_forecast_expert', content)
        self.assertIn('DecisionGovernance', content)
        self.assertIn('ranked_recommendations', content)


if __name__ == '__main__':
    unittest.main()
