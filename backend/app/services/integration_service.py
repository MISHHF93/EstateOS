from app.core.db import session_manager
from app.schemas.integrations import IntegrationCatalogResponse, IntegrationDescriptor, IntegrationWebhookAck
from app.services.base import AuditedService


class IntegrationService(AuditedService):
    def catalog(self) -> IntegrationCatalogResponse:
        items = [
            IntegrationDescriptor(
                key=binding.name,
                provider=binding.name.replace('_', ' '),
                category='azure-native',
                auth_mode=binding.auth_mode,
                status='configured',
                controls=['managed identity', 'private networking', 'audit logging'],
            )
            for binding in session_manager.integration_bindings
        ]
        return IntegrationCatalogResponse(items=items)

    def acknowledge_webhook(self, provider: str, event_type: str) -> IntegrationWebhookAck:
        routing_key = f'{provider}.{event_type}'.replace('/', '.')
        self.audit('integration_webhook', provider, 'accepted', {'event_type': event_type, 'routing_key': routing_key})
        return IntegrationWebhookAck(provider=provider, event_type=event_type, accepted=True, routing_key=routing_key)
