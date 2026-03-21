from fastapi import APIRouter

from app.schemas.users import UserMeResponse, UserPreferenceUpdate, UserPreferenceView
from app.services.user_service import UserService

router = APIRouter()
user_service = UserService()


@router.get('/me', response_model=UserMeResponse)
async def get_me() -> UserMeResponse:
    return user_service.get_me()


@router.put('/me/preferences', response_model=UserPreferenceView)
async def update_preferences(payload: UserPreferenceUpdate) -> UserPreferenceView:
    return user_service.update_preferences(payload)
