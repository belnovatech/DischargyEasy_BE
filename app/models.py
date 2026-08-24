from sqlalchemy import Column, Integer, String, Text, Boolean, Date, DateTime, Numeric
from datetime import datetime

from app.database import Base


class AdvisorCallback(Base):
    __tablename__ = "advisor_callbacks"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(100), nullable=False)

    mobile = Column(String(15), nullable=False)

    email = Column(String(150), nullable=False)

    preferred_time = Column(String(50), nullable=False)

    requirement = Column(String(150), nullable=False)

    consent = Column(Boolean, nullable=False)

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )


class ContactRequest(Base):
    __tablename__ = "contact_requests"

    id = Column(Integer, primary_key=True, index=True)

    full_name = Column(
        String(100),
        nullable=False
    )

    phone = Column(
        String(15),
        nullable=False
    )

    email = Column(
        String(150),
        nullable=False
    )

    help_type = Column(
        String(200),
        nullable=False
    )

    message = Column(
        Text,
        nullable=False
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )


class ReimbursementRequest(Base):
    __tablename__ = "reimbursement_requests"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    full_name = Column(
        String(100),
        nullable=False
    )

    mobile = Column(
        String(15),
        nullable=False
    )

    email = Column(
        String(150),
        nullable=False
    )

    city = Column(
        String(100),
        nullable=False
    )

    insurance_company = Column(
        String(150),
        nullable=False
    )

    policy_number = Column(
        String(100),
        nullable=False
    )

    hospital_name = Column(
        String(200),
        nullable=False
    )

    discharge_date = Column(
        Date,
        nullable=False
    )

    approximate_bill_amount = Column(
        Numeric(12, 2),
        nullable=True
    )

    additional_information = Column(
        Text,
        nullable=True
    )

    consent = Column(
        Boolean,
        nullable=False
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )