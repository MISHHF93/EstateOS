from uuid import uuid4

from app.models.entities import ResidencyApplication
from app.repositories.in_memory import repo
from app.schemas.residency import EligibilityAssessmentExplanation, EligibilityAssessmentRequest, EligibilityAssessmentResponse, ResidencyApplicationCreateRequest, ResidencyApplicationResponse, ResidencyProgram, ResidencyProgramsResponse
from app.services.base import AuditedService


class ResidencyService(AuditedService):
    def list_programs(self) -> ResidencyProgramsResponse:
        return ResidencyProgramsResponse(
            items=[
                ResidencyProgram(
                    id=f'program-{uuid4()}',
                    country='UAE',
                    name='Investor Residency Program',
                    status='active',
                )
            ]
        )

    def create_application(self, payload: ResidencyApplicationCreateRequest) -> ResidencyApplicationResponse:
        application = ResidencyApplication(
            program_id=payload.program_id,
            linked_property_id=payload.linked_property_id,
        )
        repo.save('residency_applications', application.id, application)
        self.audit('residency_application', application.id, 'created')
        return ResidencyApplicationResponse(
            id=application.id,
            status=application.status.value,
            program_id=application.program_id,
            linked_property_id=application.linked_property_id,
        )

    def assess(self, application_id: str, payload: EligibilityAssessmentRequest) -> EligibilityAssessmentResponse:
        self.audit('eligibility_assessment', application_id, 'generated')
        risks = [] if payload.has_clean_record else ['background verification required']
        if payload.available_investment < 500000:
            risks.append('investment budget may not meet threshold')
        if not risks:
            risks.append('document package incomplete')
        return EligibilityAssessmentResponse(
            result='preliminarily_eligible',
            score=0.82,
            explanation=EligibilityAssessmentExplanation(
                strengths=['budget meets threshold'],
                risks=risks,
            ),
        )
