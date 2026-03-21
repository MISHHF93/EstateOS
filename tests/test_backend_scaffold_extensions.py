import pathlib
import unittest


ROOT = pathlib.Path(__file__).resolve().parents[1]


class BackendScaffoldExtensionTests(unittest.TestCase):
    def test_new_bounded_contexts_and_orm_baseline_exist(self):
        expected = [
            ROOT / 'backend/app/api/v1/search.py',
            ROOT / 'backend/app/api/v1/notifications.py',
            ROOT / 'backend/app/api/v1/integrations.py',
            ROOT / 'backend/app/api/v1/platform.py',
            ROOT / 'backend/app/services/search_service.py',
            ROOT / 'backend/app/services/notification_service.py',
            ROOT / 'backend/app/services/integration_service.py',
            ROOT / 'backend/app/services/ledger_service.py',
            ROOT / 'backend/app/models/orm.py',
        ]
        for path in expected:
            with self.subTest(path=path):
                self.assertTrue(path.exists(), f'Missing scaffold file: {path}')

    def test_router_registers_new_platform_modules(self):
        content = (ROOT / 'backend/app/api/router.py').read_text(encoding='utf-8')
        for snippet in [
            "search.router",
            "notifications.router",
            "integrations.router",
            "platform.router",
        ]:
            with self.subTest(snippet=snippet):
                self.assertIn(snippet, content)

    def test_configuration_and_governance_capture_azure_and_compliance_targets(self):
        config = (ROOT / 'backend/app/core/config.py').read_text(encoding='utf-8')
        for snippet in [
            'ESTATEOS_POSTGRES_DSN',
            'ESTATEOS_REDIS_URL',
            'ESTATEOS_AZURE_BLOB_ACCOUNT_URL',
            'ESTATEOS_SERVICE_BUS_NAMESPACE',
            'ESTATEOS_KEY_VAULT_URL',
            'ESTATEOS_AZURE_OPENAI_DEPLOYMENT',
            'ISO/IEC 27017',
            'ISO/IEC 27018',
            'ISO/IEC 27701',
            'PCI DSS',
            'SOC 2 Type 2',
        ]:
            with self.subTest(snippet=snippet):
                self.assertIn(snippet, config)

    def test_event_contracts_and_tasks_cover_notifications_integrations_and_ledgering(self):
        contracts = (ROOT / 'backend/app/events/contracts.py').read_text(encoding='utf-8')
        tasks = (ROOT / 'backend/app/workers/tasks.py').read_text(encoding='utf-8')
        for snippet in ['notification.dispatched', 'integration.webhook.accepted', 'ledger.entry.posted']:
            with self.subTest(contract=snippet):
                self.assertIn(snippet, contracts)
        for snippet in ['notification-dispatch', 'integration-webhook-processing', 'ledger-closeout']:
            with self.subTest(task=snippet):
                self.assertIn(snippet, tasks)


if __name__ == '__main__':
    unittest.main()
