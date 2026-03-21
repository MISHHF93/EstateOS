from fastapi import APIRouter, status

from app.schemas.insurance import InsuranceQuotesResponse, InsuranceRequestCreateRequest, InsuranceRequestResponse
from app.services.insurance_service import InsuranceService

router = APIRouter()
insurance_service = InsuranceService()


@router.post('/requests', response_model=InsuranceRequestResponse, status_code=status.HTTP_201_CREATED)
async def create_request(payload: InsuranceRequestCreateRequest) -> InsuranceRequestResponse:
    return insurance_service.create_request(payload)


@router.get('/requests/{request_id}/quotes', response_model=InsuranceQuotesResponse)
async def get_quotes(request_id: str) -> InsuranceQuotesResponse:
    return insurance_service.get_quotes(request_id)
