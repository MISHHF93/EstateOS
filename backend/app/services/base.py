from app.core.db import AuditLogEntry, session_manager


class AuditedService:
    def audit(self, entity_type: str, entity_id: str, action: str, metadata: dict | None = None) -> None:
        session_manager.record(
            AuditLogEntry(
                entity_type=entity_type,
                entity_id=entity_id,
                action=action,
                metadata=metadata or {},
            )
        )
