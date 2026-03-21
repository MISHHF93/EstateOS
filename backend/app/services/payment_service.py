from app.models.entities import PaymentIntent
from app.models.enums import PaymentStatus
from app.repositories.in_memory import repo
from app.schemas.payments import PaymentIntentCreateRequest, PaymentIntentResponse, PaymentResponse
from app.services.base import AuditedService


class PaymentService(AuditedService):
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
