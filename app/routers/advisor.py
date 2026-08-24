from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import AdvisorCallback
from app.schemas import AdvisorCallbackCreate


router = APIRouter(
    prefix="/api/advisor",
    tags=["Advisor"]
)


@router.post("/callback")
def request_callback(
    request: AdvisorCallbackCreate,
    db: Session = Depends(get_db)
):

    try:

        advisor_request = AdvisorCallback(
            name=request.name,
            mobile=request.mobile,
            email=request.email,
            preferred_time=request.preferred_time,
            requirement=request.requirement,
            consent=request.consent
        )

        db.add(advisor_request)

        db.commit()

        db.refresh(advisor_request)

        return {
            "success": True,
            "message": "Callback request submitted successfully",
            "data": {
                "id": advisor_request.id,
                "name": advisor_request.name,
                "mobile": advisor_request.mobile,
                "email": advisor_request.email,
                "preferred_time": advisor_request.preferred_time,
                "requirement": advisor_request.requirement,
                "consent": advisor_request.consent,
                "created_at": advisor_request.created_at
            }
        }

    except Exception as e:

        db.rollback()

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )