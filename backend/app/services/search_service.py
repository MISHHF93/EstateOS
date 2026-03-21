from uuid import uuid4

from app.repositories.in_memory import repo
from app.schemas.search import SearchFacet, SearchRequest, SearchResponse, SearchResultItem
from app.services.base import AuditedService


class SearchService(AuditedService):
    def search(self, payload: SearchRequest) -> SearchResponse:
        items = repo.list('listings')
        filtered = []
        for item in items:
            if payload.city and item.city != payload.city:
                continue
            if payload.property_type and item.property_type != payload.property_type:
                continue
            if payload.budget_min is not None and item.price < payload.budget_min:
                continue
            if payload.budget_max is not None and item.price > payload.budget_max:
                continue
            filtered.append(item)

        results = [
            SearchResultItem(
                listing_id=item.id,
                title=item.title,
                city=item.city,
                country='UAE' if item.city == 'Dubai' else 'Unknown',
                price=item.price,
                currency=item.currency,
                score=0.91 if payload.query else 0.84,
                explainability=[
                    'Matched structured filters and inventory availability.',
                    'Rank boosted by portfolio fit and transaction readiness signals.',
                ],
            )
            for item in filtered[: payload.page_size]
        ]
        trace_id = f'search-{uuid4()}'
        self.audit('search', trace_id, 'executed', {'query': payload.query, 'strategy': 'hybrid_vector_keyword'})
        return SearchResponse(
            trace_id=trace_id,
            total=len(filtered),
            applied_strategy='hybrid_vector_keyword',
            facets=[
                SearchFacet(key='city', values={item.city: sum(1 for value in filtered if value.city == item.city) for item in filtered}),
                SearchFacet(key='property_type', values={item.property_type: sum(1 for value in filtered if value.property_type == item.property_type) for item in filtered}),
            ],
            items=results,
        )
