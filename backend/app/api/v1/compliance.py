from fastapi import APIRouter

from app.schemas.compliance import ComplianceCaseResponse, ScreeningCheckResponse
from app.services.compliance_service import ComplianceService

router = APIRouter()
compliance_service = ComplianceService()


@router.get('/cases/{case_id}', response_model=ComplianceCaseResponse)
async def get_case(case_id: str) -> ComplianceCaseResponse:
    return compliance_service.get_case(case_id)


@router.get('/screening-checks/{check_id}', response_model=ScreeningCheckResponse)
async def get_screening_check(check_id: str) -> ScreeningCheckResponse:
    return compliance_service.get_screening_check(check_id)
