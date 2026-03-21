from fastapi import APIRouter

from app.schemas.ai import AIAssessRequest, AIAssessResponse
from app.services.ai_orchestrator import AIOrchestratorService

router = APIRouter()
ai_service = AIOrchestratorService()


@router.post('/assess', response_model=AIAssessResponse)
async def assess(payload: AIAssessRequest) -> AIAssessResponse:
    return ai_service.assess(payload)
