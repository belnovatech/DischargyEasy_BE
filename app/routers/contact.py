from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import ContactRequest
from app.schemas import ContactRequestCreate


router = APIRouter(
    prefix="/api/contact",
    tags=["Contact"]
)


@router.post("/request")
def submit_contact_request(
    request: ContactRequestCreate,
    db: Session = Depends(get_db)
):

    try:

        contact_request = ContactRequest(
            full_name=request.full_name,
            phone=request.phone,
            email=request.email,
            help_type=request.help_type,
            message=request.message
        )

        db.add(contact_request)

        db.commit()

        db.refresh(contact_request)

        return {
            "success": True,
            "message": "Contact request submitted successfully",
            "data": {
                "id": contact_request.id,
                "full_name": contact_request.full_name,
                "phone": contact_request.phone,
                "email": contact_request.email,
                "help_type": contact_request.help_type,
                "message": contact_request.message,
                "created_at": contact_request.created_at
            }
        }

    except Exception as e:

        db.rollback()

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )