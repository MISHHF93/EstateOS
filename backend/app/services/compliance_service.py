from app.schemas.compliance import ComplianceCaseResponse, ScreeningCheckResponse
from app.services.base import AuditedService


class ComplianceService(AuditedService):
    def get_case(self, case_id: str) -> ComplianceCaseResponse:
        self.audit('compliance_case', case_id, 'retrieved')
        return ComplianceCaseResponse(id=case_id, severity='low', status='open', summary='Initial KYC review in progress.')

    def get_screening_check(self, check_id: str) -> ScreeningCheckResponse:
        self.audit('screening_check', check_id, 'retrieved')
        return ScreeningCheckResponse(
            id=check_id,
            user_id='user-demo-001',
            check_type='sanctions',
            provider='demo-provider',
            result='clear',
        )
