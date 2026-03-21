from app.schemas.common import APIModel


class UserRegistrationRequest(APIModel):
    email: str
    password: str
    role: str


class UserRegistrationResponse(APIModel):
    user_id: str
    status: str


class LoginRequest(APIModel):
    email: str
    password: str


class TokenResponse(APIModel):
    access_token: str
    refresh_token: str
    expires_in: int = 3600
