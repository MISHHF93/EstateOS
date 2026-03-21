from app.schemas.common import APIModel


class ComplianceCaseResponse(APIModel):
    id: str
    severity: str
    status: str
    summary: str


class ScreeningCheckResponse(APIModel):
    id: str
    user_id: str
    check_type: str
    provider: str
    result: str
