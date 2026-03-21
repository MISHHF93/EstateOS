from uuid import uuid4

from app.models.entities import InsuranceRequest
from app.repositories.in_memory import repo
from app.schemas.insurance import InsuranceQuote, InsuranceQuotesResponse, InsuranceRequestCreateRequest, InsuranceRequestResponse
from app.services.base import AuditedService


class InsuranceService(AuditedService):
    def create_request(self, payload: InsuranceRequestCreateRequest) -> InsuranceRequestResponse:
        request = InsuranceRequest(product_type=payload.product_type, linked_property_id=payload.linked_property_id)
        repo.save('insurance_requests', request.id, request)
        self.audit('insurance_request', request.id, 'created')
        return InsuranceRequestResponse(id=request.id, product_type=request.product_type, status='submitted')

    def get_quotes(self, request_id: str) -> InsuranceQuotesResponse:
        self.audit('insurance_request', request_id, 'quotes_viewed')
        return InsuranceQuotesResponse(
            items=[
                InsuranceQuote(
                    quote_id=f'quote-{uuid4()}',
                    partner_name='Acme Insurance',
                    premium_amount=1400,
                    currency='USD',
                    coverage_summary={'dwelling': 500000, 'liability': 300000},
                )
            ]
        )
