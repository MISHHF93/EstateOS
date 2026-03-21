from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any

from app.core.config import get_settings


@dataclass
class AuditLogEntry:
    entity_type: str
    entity_id: str
    action: str
    metadata: dict[str, Any] = field(default_factory=dict)
    created_at: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())


@dataclass
class IntegrationBinding:
    name: str
    endpoint: str
    auth_mode: str
    purpose: str


class SessionManager:
    """Lightweight infrastructure registry used by the scaffold until SQLAlchemy/driver wiring is attached."""

    def __init__(self) -> None:
        settings = get_settings()
        self.audit_logs: list[AuditLogEntry] = []
        self.connection_profile = {
            'postgres_dsn': settings.database.postgres_dsn,
            'redis_url': settings.cache.redis_url,
            'service_bus_namespace': settings.azure.service_bus_namespace,
        }
        self.integration_bindings = [
            IntegrationBinding(name='azure_blob_storage', endpoint=settings.azure.blob_account_url, auth_mode='managed_identity', purpose='document storage'),
            IntegrationBinding(name='azure_service_bus', endpoint=settings.azure.service_bus_namespace, auth_mode='managed_identity', purpose='event delivery'),
            IntegrationBinding(name='azure_key_vault', endpoint=settings.azure.key_vault_url, auth_mode='managed_identity', purpose='secret resolution'),
            IntegrationBinding(name='azure_ai_services', endpoint=settings.azure.azure_ai_project, auth_mode='managed_identity', purpose='moe inference and search'),
        ]

    def record(self, entry: AuditLogEntry) -> None:
        self.audit_logs.append(entry)


session_manager = SessionManager()
