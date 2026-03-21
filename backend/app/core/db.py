from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any


@dataclass
class AuditLogEntry:
    entity_type: str
    entity_id: str
    action: str
    metadata: dict[str, Any] = field(default_factory=dict)
    created_at: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())


class SessionManager:
    """Placeholder database/session boundary for the modular monolith scaffold."""

    def __init__(self) -> None:
        self.audit_logs: list[AuditLogEntry] = []

    def record(self, entry: AuditLogEntry) -> None:
        self.audit_logs.append(entry)


session_manager = SessionManager()
