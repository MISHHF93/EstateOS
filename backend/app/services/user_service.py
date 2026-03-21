from app.core.security import get_demo_auth_context
from app.schemas.users import UserMeResponse, UserPreferenceUpdate, UserPreferenceView, UserProfileView
from app.services.base import AuditedService


class UserService(AuditedService):
    def get_me(self) -> UserMeResponse:
        auth = get_demo_auth_context()
        return UserMeResponse(
            id=auth.user_id,
            email='user@example.com',
            roles=list(auth.roles),
            profile=UserProfileView(),
        )

    def update_preferences(self, payload: UserPreferenceUpdate) -> UserPreferenceView:
        auth = get_demo_auth_context()
        self.audit('user_preferences', auth.user_id, 'updated_preferences')
        return UserPreferenceView(user_id=auth.user_id, **payload.model_dump())
