from app.schemas.common import APIModel


class PaymentIntentCreateRequest(APIModel):
    deal_id: str | None = None
    amount: float
    currency: str
    purpose: str


class PaymentIntentResponse(APIModel):
    payment_intent_id: str
    client_secret: str
    status: str


class PaymentResponse(APIModel):
    id: str
    status: str
    amount: float
    currency: str
