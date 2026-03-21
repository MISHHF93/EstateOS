from uuid import uuid4

from app.schemas.notifications import (
    NotificationDispatchRequest,
    NotificationDispatchResponse,
    NotificationPreferenceUpdate,
    NotificationPreferenceView,
)
from app.services.base import AuditedService


class NotificationService(AuditedService):
    def update_preferences(self, user_id: str, payload: NotificationPreferenceUpdate) -> NotificationPreferenceView:
        self.audit('notification_preference', user_id, 'updated', payload.model_dump())
        return NotificationPreferenceView(user_id=user_id, **payload.model_dump())

    def dispatch(self, payload: NotificationDispatchRequest) -> NotificationDispatchResponse:
        notification_id = f'notif-{uuid4()}'
        queue = 'priority-notifications' if payload.priority == 'high' else 'notifications'
        self.audit('notification', notification_id, 'queued', {'user_id': payload.user_id, 'template_key': payload.template_key})
        return NotificationDispatchResponse(notification_id=notification_id, status='queued', queue=queue)
