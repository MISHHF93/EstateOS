from functools import lru_cache
from os import getenv

from pydantic import BaseModel, Field


class DatabaseSettings(BaseModel):
    postgres_dsn: str = Field(default_factory=lambda: getenv('ESTATEOS_POSTGRES_DSN', 'postgresql+psycopg://estateos:estateos@localhost:5432/estateos'))
    pool_size: int = Field(default_factory=lambda: int(getenv('ESTATEOS_DB_POOL_SIZE', '20')))
    max_overflow: int = Field(default_factory=lambda: int(getenv('ESTATEOS_DB_MAX_OVERFLOW', '20')))
    statement_timeout_ms: int = Field(default_factory=lambda: int(getenv('ESTATEOS_DB_STATEMENT_TIMEOUT_MS', '5000')))


class CacheSettings(BaseModel):
    redis_url: str = Field(default_factory=lambda: getenv('ESTATEOS_REDIS_URL', 'redis://localhost:6379/0'))
    default_ttl_seconds: int = Field(default_factory=lambda: int(getenv('ESTATEOS_CACHE_TTL_SECONDS', '300')))


class AzureSettings(BaseModel):
    blob_account_url: str = Field(default_factory=lambda: getenv('ESTATEOS_AZURE_BLOB_ACCOUNT_URL', 'https://example.blob.core.windows.net'))
    blob_container_documents: str = Field(default_factory=lambda: getenv('ESTATEOS_AZURE_BLOB_CONTAINER_DOCUMENTS', 'estateos-documents'))
    service_bus_namespace: str = Field(default_factory=lambda: getenv('ESTATEOS_SERVICE_BUS_NAMESPACE', 'estateos.servicebus.windows.net'))
    service_bus_topic_events: str = Field(default_factory=lambda: getenv('ESTATEOS_SERVICE_BUS_TOPIC_EVENTS', 'estateos-events'))
    key_vault_url: str = Field(default_factory=lambda: getenv('ESTATEOS_KEY_VAULT_URL', 'https://estateos-kv.vault.azure.net/'))
    azure_ai_project: str = Field(default_factory=lambda: getenv('ESTATEOS_AZURE_AI_PROJECT', 'estateos-ai-hub'))
    azure_openai_deployment: str = Field(default_factory=lambda: getenv('ESTATEOS_AZURE_OPENAI_DEPLOYMENT', 'gpt-4o-estateos'))
    azure_ai_search_index: str = Field(default_factory=lambda: getenv('ESTATEOS_AZURE_AI_SEARCH_INDEX', 'listings-index'))
    document_intelligence_model: str = Field(default_factory=lambda: getenv('ESTATEOS_DOCUMENT_INTELLIGENCE_MODEL', 'prebuilt-document'))


class SecuritySettings(BaseModel):
    jwt_issuer: str = Field(default_factory=lambda: getenv('ESTATEOS_JWT_ISSUER', 'https://identity.estateos.local'))
    jwt_audience: str = Field(default_factory=lambda: getenv('ESTATEOS_JWT_AUDIENCE', 'estateos-api'))
    access_token_ttl_seconds: int = Field(default_factory=lambda: int(getenv('ESTATEOS_ACCESS_TOKEN_TTL_SECONDS', '3600')))
    refresh_token_ttl_seconds: int = Field(default_factory=lambda: int(getenv('ESTATEOS_REFRESH_TOKEN_TTL_SECONDS', '2592000')))
    argon2_memory_cost: int = Field(default_factory=lambda: int(getenv('ESTATEOS_ARGON2_MEMORY_COST', '65536')))
    strict_transport_security: bool = Field(default_factory=lambda: getenv('ESTATEOS_STRICT_TRANSPORT_SECURITY', 'true').lower() == 'true')


class GovernanceSettings(BaseModel):
    audit_log_retention_days: int = Field(default_factory=lambda: int(getenv('ESTATEOS_AUDIT_RETENTION_DAYS', '2555')))
    pii_encryption_key_name: str = Field(default_factory=lambda: getenv('ESTATEOS_PII_ENCRYPTION_KEY_NAME', 'estateos-pii-key'))
    human_review_queue: str = Field(default_factory=lambda: getenv('ESTATEOS_HUMAN_REVIEW_QUEUE', 'compliance-and-deal-desk'))
    supported_frameworks: list[str] = Field(
        default_factory=lambda: [
            'ISO/IEC 27001',
            'ISO/IEC 27017',
            'ISO/IEC 27018',
            'ISO/IEC 27701',
            'ISO 22301',
            'ISO 31000',
            'PCI DSS',
            'SOC 2 Type 2',
            'ISO/IEC 42001',
            'ISO/IEC 5259',
        ]
    )
    sanctions_screening_provider: str = Field(default_factory=lambda: getenv('ESTATEOS_SANCTIONS_PROVIDER', 'dow-jones-or-world-check'))
    acord_version: str = Field(default_factory=lambda: getenv('ESTATEOS_ACORD_VERSION', '2.40.0'))


class Settings(BaseModel):
    app_name: str = Field(default_factory=lambda: getenv('ESTATEOS_APP_NAME', 'EstateOS Backend'))
    api_prefix: str = Field(default_factory=lambda: getenv('ESTATEOS_API_PREFIX', '/api/v1'))
    api_version: str = Field(default_factory=lambda: getenv('ESTATEOS_API_VERSION', '0.2.0'))
    environment: str = Field(default_factory=lambda: getenv('ESTATEOS_ENVIRONMENT', 'development'))
    docs_enabled: bool = Field(default_factory=lambda: getenv('ESTATEOS_DOCS_ENABLED', 'true').lower() == 'true')
    cors_origins: list[str] = Field(default_factory=lambda: [origin.strip() for origin in getenv('ESTATEOS_CORS_ORIGINS', 'http://localhost:3000,http://localhost:5173').split(',') if origin.strip()])
    database: DatabaseSettings = Field(default_factory=DatabaseSettings)
    cache: CacheSettings = Field(default_factory=CacheSettings)
    azure: AzureSettings = Field(default_factory=AzureSettings)
    security: SecuritySettings = Field(default_factory=SecuritySettings)
    governance: GovernanceSettings = Field(default_factory=GovernanceSettings)


@lru_cache
def get_settings() -> Settings:
    return Settings()
