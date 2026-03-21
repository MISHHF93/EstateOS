from app.models.entities import User
from app.repositories.in_memory import repo
from app.schemas.auth import LoginRequest, TokenResponse, UserRegistrationRequest, UserRegistrationResponse
from app.services.base import AuditedService


class AuthService(AuditedService):
    def register(self, payload: UserRegistrationRequest) -> UserRegistrationResponse:
        user = User(email=payload.email)
        repo.save('users', user.id, user)
        self.audit('user', user.id, 'registered', {'role': payload.role})
        return UserRegistrationResponse(user_id=user.id, status=user.status.value)

    def login(self, payload: LoginRequest) -> TokenResponse:
        self.audit('session', payload.email, 'login_requested')
        return TokenResponse(
            access_token=f'access-{payload.email}',
            refresh_token=f'refresh-{payload.email}',
            expires_in=3600,
        )
