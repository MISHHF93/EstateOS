from app.models.entities import PaymentIntent
from app.models.enums import PaymentStatus
from app.repositories.in_memory import repo
from app.schemas.payments import LedgerView, PaymentIntentCreateRequest, PaymentIntentResponse, PaymentResponse
from app.services.base import AuditedService
from app.services.ledger_service import LedgerService


class PaymentService(AuditedService):
    def __init__(self) -> None:
        self.ledger_service = LedgerService()

    def create_intent(self, payload: PaymentIntentCreateRequest) -> PaymentIntentResponse:
        intent = PaymentIntent(
            amount=payload.amount,
            currency=payload.currency,
            purpose=payload.purpose,
            deal_id=payload.deal_id,
        )
        repo.save('payment_intents', intent.id, intent)
        self.audit('payment_intent', intent.id, 'created', {'purpose': payload.purpose})
        return PaymentIntentResponse(
            payment_intent_id=intent.id,
            client_secret=f'secret-{intent.id}',
            status=intent.status.value,
        )

    def get_payment(self, payment_id: str) -> PaymentResponse:
        self.audit('payment', payment_id, 'retrieved')
        return PaymentResponse(id=payment_id, status=PaymentStatus.SUCCEEDED.value, amount=10000, currency='USD')

    def get_ledger_view(self, payment_id: str) -> LedgerView:
        payment = self.get_payment(payment_id)
        return self.ledger_service.view(payment_intent_id=payment.id, amount=payment.amount, currency=payment.currency)
