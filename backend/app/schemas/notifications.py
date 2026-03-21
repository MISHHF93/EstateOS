from pydantic import Field

from app.schemas.common import APIModel


class NotificationPreferenceUpdate(APIModel):
    email_enabled: bool = True
    sms_enabled: bool = False
    whatsapp_enabled: bool = False
    push_enabled: bool = True
    workflow_alerts: list[str] = Field(default_factory=lambda: ['deal_updates', 'compliance_updates', 'payment_updates'])


class NotificationPreferenceView(APIModel):
    user_id: str
    email_enabled: bool
    sms_enabled: bool
    whatsapp_enabled: bool
    push_enabled: bool
    workflow_alerts: list[str]


class NotificationDispatchRequest(APIModel):
    user_id: str
    template_key: str
    channel: str
    variables: dict = Field(default_factory=dict)
    priority: str = 'normal'


class NotificationDispatchResponse(APIModel):
    notification_id: str
    status: str
    queue: str
