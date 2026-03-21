from app.schemas.common import APIModel


class ResidencyProgram(APIModel):
    id: str
    country: str
    name: str
    status: str


class ResidencyProgramsResponse(APIModel):
    items: list[ResidencyProgram]


class ResidencyApplicationCreateRequest(APIModel):
    program_id: str
    linked_property_id: str | None = None


class ResidencyApplicationResponse(APIModel):
    id: str
    status: str
    program_id: str
    linked_property_id: str | None = None


class EligibilityAssessmentRequest(APIModel):
    household_size: int
    available_investment: float
    has_clean_record: bool


class EligibilityAssessmentExplanation(APIModel):
    strengths: list[str]
    risks: list[str]


class EligibilityAssessmentResponse(APIModel):
    result: str
    score: float
    explanation: EligibilityAssessmentExplanation
