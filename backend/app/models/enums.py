from enum import StrEnum


class UserStatus(StrEnum):
    PENDING_VERIFICATION = 'pending_verification'
    ACTIVE = 'active'
    SUSPENDED = 'suspended'


class ListingStatus(StrEnum):
    DRAFT = 'draft'
    PUBLISHED = 'published'
    ARCHIVED = 'archived'


class DealStatus(StrEnum):
    OPEN = 'open'
    CLOSED = 'closed'
    CANCELLED = 'cancelled'


class DealStage(StrEnum):
    OFFER_SUBMITTED = 'offer_submitted'
    UNDER_REVIEW = 'under_review'
    DUE_DILIGENCE = 'due_diligence'
    CLOSED = 'closed'


class DocumentStatus(StrEnum):
    PENDING_UPLOAD = 'pending_upload'
    UPLOADED = 'uploaded'
    VERIFIED = 'verified'


class ResidencyStatus(StrEnum):
    DRAFT = 'draft'
    SUBMITTED = 'submitted'
    PRELIMINARILY_ELIGIBLE = 'preliminarily_eligible'


class PaymentStatus(StrEnum):
    REQUIRES_PAYMENT_METHOD = 'requires_payment_method'
    SUCCEEDED = 'succeeded'
    FAILED = 'failed'


class ComplianceSeverity(StrEnum):
    LOW = 'low'
    MEDIUM = 'medium'
    HIGH = 'high'
