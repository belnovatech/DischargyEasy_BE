from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import ReimbursementRequest
from app.schemas import ReimbursementRequestCreate


router = APIRouter(
    prefix="/api/reimbursement",
    tags=["Reimbursement"]
)


@router.post("/request")
def submit_reimbursement_request(
    request: ReimbursementRequestCreate,
    db: Session = Depends(get_db)
):

    try:

        reimbursement_request = ReimbursementRequest(

            full_name=request.full_name,

            mobile=request.mobile,

            email=request.email,

            city=request.city,

            insurance_company=request.insurance_company,

            policy_number=request.policy_number,

            hospital_name=request.hospital_name,

            discharge_date=request.discharge_date,

            approximate_bill_amount=request.approximate_bill_amount,

            additional_information=request.additional_information,

            consent=request.consent
        )

        db.add(reimbursement_request)

        db.commit()

        db.refresh(reimbursement_request)

        return {

            "success": True,

            "message": "Reimbursement request submitted successfully",

            "data": {

                "id": reimbursement_request.id,

                "full_name": reimbursement_request.full_name,

                "mobile": reimbursement_request.mobile,

                "email": reimbursement_request.email,

                "city": reimbursement_request.city,

                "insurance_company":
                    reimbursement_request.insurance_company,

                "policy_number":
                    reimbursement_request.policy_number,

                "hospital_name":
                    reimbursement_request.hospital_name,

                "discharge_date":
                    reimbursement_request.discharge_date,

                "approximate_bill_amount":
                    reimbursement_request.approximate_bill_amount,

                "additional_information":
                    reimbursement_request.additional_information,

                "consent":
                    reimbursement_request.consent,

                "created_at":
                    reimbursement_request.created_at
            }
        }

    except Exception as e:

        db.rollback()

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )