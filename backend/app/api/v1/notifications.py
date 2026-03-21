from fastapi import APIRouter, status

from app.core.security import get_demo_auth_context
from app.schemas.notifications import (
    NotificationDispatchRequest,
    NotificationDispatchResponse,
    NotificationPreferenceUpdate,
    NotificationPreferenceView,
)
from app.services.notification_service import NotificationService

router = APIRouter()
notification_service = NotificationService()


@router.put('/preferences', response_model=NotificationPreferenceView, summary='Update notification routing preferences')
async def update_preferences(payload: NotificationPreferenceUpdate) -> NotificationPreferenceView:
    return notification_service.update_preferences(get_demo_auth_context().user_id, payload)


@router.post('/dispatch', response_model=NotificationDispatchResponse, status_code=status.HTTP_202_ACCEPTED, summary='Queue a notification dispatch job')
async def dispatch(payload: NotificationDispatchRequest) -> NotificationDispatchResponse:
    return notification_service.dispatch(payload)
