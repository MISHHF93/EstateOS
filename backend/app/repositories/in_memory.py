from collections import defaultdict
from typing import Any


class InMemoryRepository:
    def __init__(self) -> None:
        self._store: dict[str, dict[str, Any]] = defaultdict(dict)

    def save(self, collection: str, item_id: str, value: Any) -> Any:
        self._store[collection][item_id] = value
        return value

    def get(self, collection: str, item_id: str) -> Any | None:
        return self._store[collection].get(item_id)

    def list(self, collection: str) -> list[Any]:
        return list(self._store[collection].values())


repo = InMemoryRepository()
