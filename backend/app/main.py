from fastapi import FastAPI

from app.api.router import api_router
from app.core.config import get_settings
from app.core.logging import configure_logging


def create_app() -> FastAPI:
    settings = get_settings()
    configure_logging()

    application = FastAPI(
        title=settings.app_name,
        version=settings.api_version,
        openapi_url=f"{settings.api_prefix}/openapi.json",
        docs_url=f"{settings.api_prefix}/docs",
        redoc_url=f"{settings.api_prefix}/redoc",
    )
    application.include_router(api_router, prefix=settings.api_prefix)

    @application.get('/health', tags=['platform'])
    async def healthcheck() -> dict[str, str]:
        return {'status': 'ok', 'service': settings.app_name}

    return application


app = create_app()
