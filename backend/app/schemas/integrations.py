from pydantic import Field

from app.schemas.common import APIModel


class IntegrationDescriptor(APIModel):
    key: str
    provider: str
    category: str
    auth_mode: str
    status: str
    controls: list[str] = Field(default_factory=list)


class IntegrationCatalogResponse(APIModel):
    items: list[IntegrationDescriptor]


class IntegrationWebhookAck(APIModel):
    provider: str
    event_type: str
    accepted: bool
    routing_key: str
