from fastapi import APIRouter, Query, status

from app.schemas.listings import ListingCreateRequest, ListingDetailResponse, ListingListResponse, ListingSummary, FavoriteCreateRequest
from app.services.listing_service import ListingService

router = APIRouter()
listing_service = ListingService()


@router.get('', response_model=ListingListResponse)
async def list_listings(
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
    city: str | None = None,
    min_price: float | None = None,
    max_price: float | None = None,
    property_type: str | None = None,
) -> ListingListResponse:
    return listing_service.list_listings(page, page_size, city, min_price, max_price, property_type)


@router.post('', response_model=ListingDetailResponse, status_code=status.HTTP_201_CREATED)
async def create_listing(payload: ListingCreateRequest) -> ListingDetailResponse:
    return listing_service.create_listing(payload)


@router.get('/{listing_id}', response_model=ListingDetailResponse)
async def get_listing(listing_id: str) -> ListingDetailResponse:
    return listing_service.get_listing(listing_id)


@router.post('/favorites', response_model=ListingSummary, status_code=status.HTTP_201_CREATED)
async def favorite_listing(payload: FavoriteCreateRequest) -> ListingSummary:
    return listing_service.favorite_listing(payload)
