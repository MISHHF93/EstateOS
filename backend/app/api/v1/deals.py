from fastapi import APIRouter, status

from app.schemas.deals import DealCreateRequest, DealDetailResponse, OfferCreateRequest, OfferResponse
from app.services.deal_service import DealService

router = APIRouter()
deal_service = DealService()


@router.post('', response_model=DealDetailResponse, status_code=status.HTTP_201_CREATED)
async def create_deal(payload: DealCreateRequest) -> DealDetailResponse:
    return deal_service.create_deal(payload)


@router.post('/{deal_id}/offers', response_model=OfferResponse, status_code=status.HTTP_201_CREATED)
async def create_offer(deal_id: str, payload: OfferCreateRequest) -> OfferResponse:
    return deal_service.create_offer(deal_id, payload)


@router.get('/{deal_id}', response_model=DealDetailResponse)
async def get_deal(deal_id: str) -> DealDetailResponse:
    return deal_service.get_deal(deal_id)
