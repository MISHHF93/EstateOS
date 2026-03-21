from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.router import api_router
from app.core.config import get_settings
from app.core.logging import configure_logging


@asynccontextmanager
async def lifespan(_: FastAPI):
    configure_logging()
    yield


def create_app() -> FastAPI:
    settings = get_settings()

    application = FastAPI(
        title=settings.app_name,
        version=settings.api_version,
        openapi_url=f"{settings.api_prefix}/openapi.json",
        docs_url=f"{settings.api_prefix}/docs" if settings.docs_enabled else None,
        redoc_url=f"{settings.api_prefix}/redoc" if settings.docs_enabled else None,
        summary='AI-native real estate operating system backend scaffold built around a governed MoE orchestration layer.',
        description=(
            'Production-grade FastAPI scaffold for EstateOS covering identity, RBAC, profiles, listings, search, '
            'deals, documents, residency-by-investment, insurance, payments, ledgering, compliance, notifications, '
            'third-party integrations, and explainable AI orchestration.'
        ),
        lifespan=lifespan,
        contact={'name': 'EstateOS Platform Engineering', 'email': 'platform@example.com'},
        license_info={'name': 'Proprietary reference scaffold'},
    )
    application.add_middleware(
        CORSMiddleware,
        allow_origins=settings.cors_origins,
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*'],
    )
    application.include_router(api_router, prefix=settings.api_prefix)

    @application.get('/health', tags=['platform'], summary='Basic platform liveness probe')
    async def healthcheck() -> dict[str, str]:
        return {'status': 'ok', 'service': settings.app_name, 'version': settings.api_version}

    return application


app = create_app()
