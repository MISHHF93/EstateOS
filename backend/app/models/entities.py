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
class Role:
    name: str
    description: str
    id: str = field(default_factory=lambda: new_id('role'))
    created_at: str = field(default_factory=utcnow)


@dataclass
class User:
    email: str
    auth_provider: str = 'password'
    status: UserStatus = UserStatus.PENDING_VERIFICATION
    id: str = field(default_factory=lambda: new_id('user'))
    created_at: str = field(default_factory=utcnow)
    updated_at: str = field(default_factory=utcnow)


@dataclass
class UserRole:
    user_id: str
    role_id: str
    id: str = field(default_factory=lambda: new_id('userrole'))
    assigned_at: str = field(default_factory=utcnow)


@dataclass
class UserProfile:
    user_id: str
    first_name: str
    last_name: str
    investor_type: str
    residency_goal: str | None = None
    risk_appetite: str = 'balanced'
    preferred_countries: list[str] = field(default_factory=list)
    privacy_tier: str = 'standard'
    id: str = field(default_factory=lambda: new_id('profile'))
    created_at: str = field(default_factory=utcnow)
    updated_at: str = field(default_factory=utcnow)


@dataclass
class Property:
    title: str
    property_type: str
    country: str
    city: str
    address_line: str
    bedrooms: int
    bathrooms: int
    square_meters: float
    climate_risk: str = 'low'
    energy_rating: str = 'pending'
    id: str = field(default_factory=lambda: new_id('property'))
    created_at: str = field(default_factory=utcnow)
    updated_at: str = field(default_factory=utcnow)


@dataclass
class Listing:
    title: str
    price: float
    currency: str
    city: str
    property_type: str
    property_id: str | None = None
    broker_user_id: str | None = None
    id: str = field(default_factory=lambda: new_id('listing'))
    status: ListingStatus = ListingStatus.PUBLISHED
    bedrooms: int = 0
    bathrooms: int = 0
    description: str = ''
    thumbnail_url: str = 'https://example.com/listing.jpg'
    created_at: str = field(default_factory=utcnow)
    updated_at: str = field(default_factory=utcnow)


@dataclass
class Deal:
    listing_id: str
    deal_type: str
    offer_amount: float
    currency: str
    buyer_user_id: str | None = None
    seller_user_id: str | None = None
    id: str = field(default_factory=lambda: new_id('deal'))
    status: DealStatus = DealStatus.OPEN
    stage: DealStage = DealStage.OFFER_SUBMITTED
    milestones: list[dict[str, Any]] = field(default_factory=list)
    created_at: str = field(default_factory=utcnow)
    updated_at: str = field(default_factory=utcnow)


@dataclass
class DealParticipant:
    deal_id: str
    user_id: str
    participant_role: str
    id: str = field(default_factory=lambda: new_id('dealpart'))
    created_at: str = field(default_factory=utcnow)


@dataclass
class Document:
    file_name: str
    category: str
    context_type: str
    context_id: str
    owner_user_id: str | None = None
    blob_path: str | None = None
    id: str = field(default_factory=lambda: new_id('doc'))
    status: DocumentStatus = DocumentStatus.PENDING_UPLOAD
    upload_url: str = field(init=False)
    created_at: str = field(default_factory=utcnow)
    updated_at: str = field(default_factory=utcnow)

    def __post_init__(self) -> None:
        self.upload_url = f'https://storage.example.com/upload/{self.id}'


@dataclass
class ResidencyApplication:
    user_id: str
    program_id: str
    linked_property_id: str | None = None
    country: str | None = None
    investment_amount: float | None = None
    id: str = field(default_factory=lambda: new_id('resapp'))
    status: ResidencyStatus = ResidencyStatus.DRAFT
    created_at: str = field(default_factory=utcnow)
    updated_at: str = field(default_factory=utcnow)


@dataclass
class InsuranceRequest:
    user_id: str
    product_type: str
    linked_property_id: str | None = None
    coverage_amount: float | None = None
    acord_payload_id: str | None = None
    id: str = field(default_factory=lambda: new_id('insreq'))
    created_at: str = field(default_factory=utcnow)
    updated_at: str = field(default_factory=utcnow)


@dataclass
class PaymentIntent:
    amount: float
    currency: str
    purpose: str
    deal_id: str | None = None
    payer_user_id: str | None = None
    payment_provider: str = 'stripe'
    id: str = field(default_factory=lambda: new_id('pi'))
    status: PaymentStatus = PaymentStatus.REQUIRES_PAYMENT_METHOD
    created_at: str = field(default_factory=utcnow)
    updated_at: str = field(default_factory=utcnow)


@dataclass
class ComplianceCase:
    summary: str
    subject_user_id: str | None = None
    jurisdiction: str | None = None
    id: str = field(default_factory=lambda: new_id('case'))
    severity: ComplianceSeverity = ComplianceSeverity.LOW
    status: str = 'open'
    created_at: str = field(default_factory=utcnow)
    updated_at: str = field(default_factory=utcnow)


@dataclass
class AIRequest:
    user_id: str
    intent: str
    selected_experts: list[str]
    release_status: str
    id: str = field(default_factory=lambda: new_id('aireq'))
    created_at: str = field(default_factory=utcnow)
    metadata: dict[str, Any] = field(default_factory=dict)
