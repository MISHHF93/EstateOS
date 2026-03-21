"""SQLAlchemy ORM baseline for the production-grade EstateOS backend.

This module is intentionally not imported by the demo services so the scaffold can remain lightweight,
but it provides build-ready table declarations for teams wiring Alembic migrations and async sessions.
"""

from sqlalchemy import JSON, Boolean, DateTime, Float, ForeignKey, Integer, Numeric, String, Text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy.sql import func


class Base(DeclarativeBase):
    pass


class TimestampMixin:
    created_at: Mapped[DateTime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[DateTime] = mapped_column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())


class UserORM(TimestampMixin, Base):
    __tablename__ = 'users'

    id: Mapped[str] = mapped_column(String(64), primary_key=True)
    email: Mapped[str] = mapped_column(String(320), unique=True, index=True)
    hashed_password: Mapped[str] = mapped_column(String(255))
    status: Mapped[str] = mapped_column(String(32), index=True)
    auth_provider: Mapped[str] = mapped_column(String(32), default='password')
    profiles: Mapped[list['UserProfileORM']] = relationship(back_populates='user')


class UserProfileORM(TimestampMixin, Base):
    __tablename__ = 'user_profiles'

    id: Mapped[str] = mapped_column(String(64), primary_key=True)
    user_id: Mapped[str] = mapped_column(ForeignKey('users.id'), index=True)
    first_name: Mapped[str] = mapped_column(String(120))
    last_name: Mapped[str] = mapped_column(String(120))
    residency_goal: Mapped[str | None] = mapped_column(String(120))
    investor_type: Mapped[str] = mapped_column(String(60))
    risk_appetite: Mapped[str] = mapped_column(String(32), default='balanced')
    privacy_tier: Mapped[str] = mapped_column(String(32), default='standard')
    preferences: Mapped[dict] = mapped_column(JSON, default=dict)
    user: Mapped[UserORM] = relationship(back_populates='profiles')


class PropertyORM(TimestampMixin, Base):
    __tablename__ = 'properties'

    id: Mapped[str] = mapped_column(String(64), primary_key=True)
    title: Mapped[str] = mapped_column(String(255))
    country: Mapped[str] = mapped_column(String(120), index=True)
    city: Mapped[str] = mapped_column(String(120), index=True)
    property_type: Mapped[str] = mapped_column(String(60), index=True)
    address_line: Mapped[str] = mapped_column(String(255))
    bedrooms: Mapped[int] = mapped_column(Integer)
    bathrooms: Mapped[int] = mapped_column(Integer)
    square_meters: Mapped[float] = mapped_column(Float)
    climate_risk: Mapped[str] = mapped_column(String(32), default='low')
    listings: Mapped[list['ListingORM']] = relationship(back_populates='property')


class ListingORM(TimestampMixin, Base):
    __tablename__ = 'listings'

    id: Mapped[str] = mapped_column(String(64), primary_key=True)
    property_id: Mapped[str] = mapped_column(ForeignKey('properties.id'), index=True)
    broker_user_id: Mapped[str | None] = mapped_column(String(64), index=True)
    title: Mapped[str] = mapped_column(String(255), index=True)
    description: Mapped[str] = mapped_column(Text)
    status: Mapped[str] = mapped_column(String(32), index=True)
    price: Mapped[float] = mapped_column(Numeric(14, 2))
    currency: Mapped[str] = mapped_column(String(3))
    personalization_signals: Mapped[dict] = mapped_column(JSON, default=dict)
    property: Mapped[PropertyORM] = relationship(back_populates='listings')


class DealORM(TimestampMixin, Base):
    __tablename__ = 'deals'

    id: Mapped[str] = mapped_column(String(64), primary_key=True)
    listing_id: Mapped[str] = mapped_column(ForeignKey('listings.id'), index=True)
    buyer_user_id: Mapped[str | None] = mapped_column(String(64), index=True)
    seller_user_id: Mapped[str | None] = mapped_column(String(64), index=True)
    stage: Mapped[str] = mapped_column(String(32), index=True)
    status: Mapped[str] = mapped_column(String(32), index=True)
    offer_amount: Mapped[float] = mapped_column(Numeric(14, 2))
    workflow_state: Mapped[dict] = mapped_column(JSON, default=dict)


class PaymentLedgerEntryORM(TimestampMixin, Base):
    __tablename__ = 'payment_ledger_entries'

    id: Mapped[str] = mapped_column(String(64), primary_key=True)
    payment_intent_id: Mapped[str] = mapped_column(String(64), index=True)
    deal_id: Mapped[str | None] = mapped_column(String(64), index=True)
    entry_type: Mapped[str] = mapped_column(String(32), index=True)
    amount: Mapped[float] = mapped_column(Numeric(14, 2))
    currency: Mapped[str] = mapped_column(String(3))
    status: Mapped[str] = mapped_column(String(32), index=True)
    immutable_hash: Mapped[str] = mapped_column(String(128), unique=True)


class ComplianceCaseORM(TimestampMixin, Base):
    __tablename__ = 'compliance_cases'

    id: Mapped[str] = mapped_column(String(64), primary_key=True)
    subject_user_id: Mapped[str | None] = mapped_column(String(64), index=True)
    jurisdiction: Mapped[str | None] = mapped_column(String(120), index=True)
    severity: Mapped[str] = mapped_column(String(32), index=True)
    status: Mapped[str] = mapped_column(String(32), index=True)
    summary: Mapped[str] = mapped_column(Text)
    screening_snapshot: Mapped[dict] = mapped_column(JSON, default=dict)
    manual_review_required: Mapped[bool] = mapped_column(Boolean, default=False)
