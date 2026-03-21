from uuid import uuid4

from app.models.entities import Deal
from app.repositories.in_memory import repo
from app.schemas.deals import DealCreateRequest, DealDetailResponse, MilestoneView, OfferCreateRequest, OfferResponse
from app.services.base import AuditedService


class DealService(AuditedService):
    def create_deal(self, payload: DealCreateRequest) -> DealDetailResponse:
        milestones = [
            {'code': 'kyc_check', 'status': 'completed'},
            {'code': 'deposit_payment', 'status': 'pending'},
        ]
        deal = Deal(
            listing_id=payload.listing_id,
            deal_type=payload.deal_type,
            offer_amount=payload.offer_amount,
            currency=payload.currency,
            milestones=milestones,
        )
        repo.save('deals', deal.id, deal)
        self.audit('deal', deal.id, 'created', {'listing_id': payload.listing_id})
        return self._detail(deal)

    def create_offer(self, deal_id: str, payload: OfferCreateRequest) -> OfferResponse:
        offer_id = f'offer-{uuid4()}'
        self.audit('offer', offer_id, 'created', {'deal_id': deal_id})
        return OfferResponse(id=offer_id, amount=payload.amount, currency=payload.currency, status='submitted')

    def get_deal(self, deal_id: str) -> DealDetailResponse:
        deal = repo.get('deals', deal_id)
        if deal is None:
            deal = self.create_deal(DealCreateRequest(listing_id='listing-demo-001', deal_type='purchase', offer_amount=530000, currency='USD'))
            return deal
        return self._detail(deal)

    def _detail(self, deal: Deal) -> DealDetailResponse:
        return DealDetailResponse(
            id=deal.id,
            status=deal.status.value,
            stage=deal.stage.value,
            milestones=[MilestoneView(**milestone) for milestone in deal.milestones],
        )
