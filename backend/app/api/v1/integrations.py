from fastapi import APIRouter

from app.schemas.integrations import IntegrationCatalogResponse, IntegrationWebhookAck
from app.services.integration_service import IntegrationService

router = APIRouter()
integration_service = IntegrationService()


@router.get('', response_model=IntegrationCatalogResponse, summary='List configured third-party integrations')
async def list_integrations() -> IntegrationCatalogResponse:
    return integration_service.catalog()


@router.post('/webhooks/{provider}/{event_type}', response_model=IntegrationWebhookAck, summary='Accept and route partner webhooks')
async def acknowledge_webhook(provider: str, event_type: str) -> IntegrationWebhookAck:
    return integration_service.acknowledge_webhook(provider, event_type)
