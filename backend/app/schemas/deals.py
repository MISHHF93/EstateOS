from app.schemas.common import APIModel


class DealCreateRequest(APIModel):
    listing_id: str
    deal_type: str
    offer_amount: float
    currency: str


class MilestoneView(APIModel):
    code: str
    status: str


class DealDetailResponse(APIModel):
    id: str
    status: str
    stage: str
    milestones: list[MilestoneView]


class OfferCreateRequest(APIModel):
    amount: float
    currency: str
    terms: dict[str, str | int | float | bool] = {}


class OfferResponse(APIModel):
    id: str
    amount: float
    currency: str
    status: str
