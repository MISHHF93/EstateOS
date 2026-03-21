from fastapi import APIRouter, status

from app.schemas.search import SearchRequest, SearchResponse
from app.services.search_service import SearchService

router = APIRouter()
search_service = SearchService()


@router.post('', response_model=SearchResponse, status_code=status.HTTP_200_OK, summary='Run explainable hybrid property search')
async def search(payload: SearchRequest) -> SearchResponse:
    return search_service.search(payload)
