from fastapi import APIRouter, status

from app.schemas.payments import LedgerView, PaymentIntentCreateRequest, PaymentIntentResponse, PaymentResponse
from app.services.payment_service import PaymentService

router = APIRouter()
payment_service = PaymentService()


@router.post('/intents', response_model=PaymentIntentResponse, status_code=status.HTTP_201_CREATED)
async def create_intent(payload: PaymentIntentCreateRequest) -> PaymentIntentResponse:
    return payment_service.create_intent(payload)


@router.get('/{payment_id}', response_model=PaymentResponse)
async def get_payment(payment_id: str) -> PaymentResponse:
    return payment_service.get_payment(payment_id)


@router.get('/{payment_id}/ledger', response_model=LedgerView, summary='Retrieve immutable ledger view for a payment')
async def get_payment_ledger(payment_id: str) -> LedgerView:
    return payment_service.get_ledger_view(payment_id)
