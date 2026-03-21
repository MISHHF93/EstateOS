from pydantic import Field

from app.schemas.common import APIModel


class SearchRequest(APIModel):
    query: str | None = None
    city: str | None = None
    country: str | None = None
    property_type: str | None = None
    budget_min: float | None = None
    budget_max: float | None = None
    residency_eligible: bool | None = None
    investor_profile: str | None = None
    sort_by: str = 'relevance'
    page: int = 1
    page_size: int = 20


class SearchFacet(APIModel):
    key: str
    values: dict[str, int] = Field(default_factory=dict)


class SearchResultItem(APIModel):
    listing_id: str
    title: str
    city: str
    country: str
    price: float
    currency: str
    score: float
    explainability: list[str]


class SearchResponse(APIModel):
    trace_id: str
    total: int
    applied_strategy: str
    facets: list[SearchFacet]
    items: list[SearchResultItem]
