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


class LedgerEntry(APIModel):
    id: str
    payment_intent_id: str
    deal_id: str | None = None
    entry_type: str
    amount: float
    currency: str
    immutable_hash: str
    status: str


class LedgerView(APIModel):
    entries: list[LedgerEntry]
    release_controls: list[str]
