from hashlib import sha256
from uuid import uuid4

from app.schemas.payments import LedgerEntry, LedgerView
from app.services.base import AuditedService


class LedgerService(AuditedService):
    def post_entry(self, payment_intent_id: str, amount: float, currency: str, entry_type: str, deal_id: str | None = None) -> LedgerEntry:
        entry_id = f'ledger-{uuid4()}'
        immutable_hash = sha256(f'{payment_intent_id}:{amount}:{currency}:{entry_type}:{deal_id}'.encode()).hexdigest()
        self.audit('ledger_entry', entry_id, 'posted', {'payment_intent_id': payment_intent_id, 'entry_type': entry_type})
        return LedgerEntry(
            id=entry_id,
            payment_intent_id=payment_intent_id,
            deal_id=deal_id,
            entry_type=entry_type,
            amount=amount,
            currency=currency,
            immutable_hash=immutable_hash,
            status='posted',
        )

    def view(self, payment_intent_id: str, amount: float, currency: str, deal_id: str | None = None) -> LedgerView:
        entry = self.post_entry(payment_intent_id=payment_intent_id, amount=amount, currency=currency, entry_type='escrow_reservation', deal_id=deal_id)
        return LedgerView(entries=[entry], release_controls=['dual approval for refunds', 'fraud gate before settlement', 'PCI DSS evidence retained'])
