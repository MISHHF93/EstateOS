from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any
from uuid import uuid4

from app.models.enums import ComplianceSeverity, DealStage, DealStatus, DocumentStatus, ListingStatus, PaymentStatus, ResidencyStatus, UserStatus


def utcnow() -> str:
    return datetime.now(timezone.utc).isoformat()


def new_id(prefix: str) -> str:
    return f'{prefix}-{uuid4()}'


@dataclass
class User:
    email: str
    auth_provider: str = 'password'
    status: UserStatus = UserStatus.PENDING_VERIFICATION
    id: str = field(default_factory=lambda: new_id('user'))
    created_at: str = field(default_factory=utcnow)
    updated_at: str = field(default_factory=utcnow)


@dataclass
class Listing:
    title: str
    price: float
    currency: str
    city: str
    property_type: str
    id: str = field(default_factory=lambda: new_id('listing'))
    status: ListingStatus = ListingStatus.PUBLISHED
    bedrooms: int = 0
    bathrooms: int = 0
    description: str = ''
    thumbnail_url: str = 'https://example.com/listing.jpg'


@dataclass
class Deal:
    listing_id: str
    deal_type: str
    offer_amount: float
    currency: str
    id: str = field(default_factory=lambda: new_id('deal'))
    status: DealStatus = DealStatus.OPEN
    stage: DealStage = DealStage.OFFER_SUBMITTED
    milestones: list[dict[str, Any]] = field(default_factory=list)


@dataclass
class Document:
    file_name: str
    category: str
    context_type: str
    context_id: str
    id: str = field(default_factory=lambda: new_id('doc'))
    status: DocumentStatus = DocumentStatus.PENDING_UPLOAD
    upload_url: str = field(init=False)

    def __post_init__(self) -> None:
        self.upload_url = f'https://storage.example.com/upload/{self.id}'


@dataclass
class ResidencyApplication:
    program_id: str
    linked_property_id: str | None = None
    id: str = field(default_factory=lambda: new_id('resapp'))
    status: ResidencyStatus = ResidencyStatus.DRAFT


@dataclass
class InsuranceRequest:
    product_type: str
    linked_property_id: str | None = None
    id: str = field(default_factory=lambda: new_id('insreq'))


@dataclass
class PaymentIntent:
    amount: float
    currency: str
    purpose: str
    deal_id: str | None = None
    id: str = field(default_factory=lambda: new_id('pi'))
    status: PaymentStatus = PaymentStatus.REQUIRES_PAYMENT_METHOD


@dataclass
class ComplianceCase:
    summary: str
    id: str = field(default_factory=lambda: new_id('case'))
    severity: ComplianceSeverity = ComplianceSeverity.LOW
    status: str = 'open'
