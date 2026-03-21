from app.schemas.common import APIModel


class InsuranceRequestCreateRequest(APIModel):
    linked_property_id: str | None = None
    product_type: str
    input_payload: dict


class InsuranceRequestResponse(APIModel):
    id: str
    product_type: str
    status: str


class InsuranceQuote(APIModel):
    quote_id: str
    partner_name: str
    premium_amount: float
    currency: str
    coverage_summary: dict


class InsuranceQuotesResponse(APIModel):
    items: list[InsuranceQuote]
