from app.schemas.common import APIModel


class PlatformReadinessResponse(APIModel):
    service: str
    version: str
    environment: str
    infrastructure: dict[str, str]
    governance_frameworks: list[str]
