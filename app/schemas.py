from datetime import date
from decimal import Decimal

from pydantic import BaseModel, EmailStr, ConfigDict


class AdvisorCallbackCreate(BaseModel):
    name: str
    mobile: str
    email: EmailStr
    preferred_time: str
    requirement: str
    consent: bool


class AdvisorCallbackResponse(AdvisorCallbackCreate):
    id: int

    model_config = ConfigDict(from_attributes=True)




class ContactRequestCreate(BaseModel):
    full_name: str
    phone: str
    email: EmailStr
    help_type: str
    message: str


class ContactRequestResponse(ContactRequestCreate):
    id: int

    model_config = ConfigDict(from_attributes=True)




class ReimbursementRequestCreate(BaseModel):
    full_name: str
    mobile: str
    email: EmailStr
    city: str
    insurance_company: str
    policy_number: str
    hospital_name: str
    discharge_date: date
    approximate_bill_amount: Decimal | None = None
    additional_information: str | None = None
    consent: bool


class ReimbursementRequestResponse(ReimbursementRequestCreate):
    id: int

    model_config = ConfigDict(from_attributes=True)