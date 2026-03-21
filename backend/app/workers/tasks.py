from dataclasses import dataclass


@dataclass(frozen=True)
class DeferredTask:
    name: str
    queue: str
    description: str


TASK_CATALOG = [
    DeferredTask(name='document-extraction', queue='documents', description='Run OCR and classification for uploaded documents.'),
    DeferredTask(name='listing-index', queue='search', description='Project listing updates into the search index.'),
    DeferredTask(name='residency-assessment', queue='workflow', description='Run asynchronous residency eligibility scoring.'),
]
