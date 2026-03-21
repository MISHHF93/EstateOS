from fastapi import APIRouter, status

from app.schemas.residency import EligibilityAssessmentRequest, EligibilityAssessmentResponse, ResidencyApplicationCreateRequest, ResidencyApplicationResponse, ResidencyProgramsResponse
from app.services.residency_service import ResidencyService

router = APIRouter()
residency_service = ResidencyService()


@router.get('/programs', response_model=ResidencyProgramsResponse)
async def list_programs() -> ResidencyProgramsResponse:
    return residency_service.list_programs()


@router.post('/applications', response_model=ResidencyApplicationResponse, status_code=status.HTTP_201_CREATED)
async def create_application(payload: ResidencyApplicationCreateRequest) -> ResidencyApplicationResponse:
    return residency_service.create_application(payload)


@router.post('/applications/{application_id}/assess', response_model=EligibilityAssessmentResponse)
async def assess_application(application_id: str, payload: EligibilityAssessmentRequest) -> EligibilityAssessmentResponse:
    return residency_service.assess(application_id, payload)
