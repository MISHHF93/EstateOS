from fastapi import APIRouter

from app.core.config import get_settings
from app.core.db import session_manager
from app.schemas.platform import PlatformReadinessResponse

router = APIRouter()


@router.get('/readiness', response_model=PlatformReadinessResponse, summary='Retrieve platform deployment readiness summary')
async def readiness() -> PlatformReadinessResponse:
    settings = get_settings()
    return PlatformReadinessResponse(
        service=settings.app_name,
        version=settings.api_version,
        environment=settings.environment,
        infrastructure=session_manager.connection_profile,
        governance_frameworks=settings.governance.supported_frameworks,
    )
