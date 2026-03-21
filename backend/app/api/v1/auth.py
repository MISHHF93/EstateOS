from fastapi import APIRouter, status

from app.schemas.auth import LoginRequest, TokenResponse, UserRegistrationRequest, UserRegistrationResponse
from app.services.auth_service import AuthService

router = APIRouter()
auth_service = AuthService()


@router.post('/register', response_model=UserRegistrationResponse, status_code=status.HTTP_201_CREATED)
async def register(payload: UserRegistrationRequest) -> UserRegistrationResponse:
    return auth_service.register(payload)


@router.post('/login', response_model=TokenResponse)
async def login(payload: LoginRequest) -> TokenResponse:
    return auth_service.login(payload)
