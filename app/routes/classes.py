from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from starlette import status
from app.database import SessionLocal
from app.models import FitnessClassModel
from app.schemas import ResponseModel, FitnessClassOut

router = APIRouter(prefix="/classes", tags=["Classes"])

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/", response_model=ResponseModel[List[FitnessClassOut]])
def get_classes(db: Session = Depends(get_db)):
    """Fetch all upcoming fitness classes."""
    classes = db.query(FitnessClassModel).all()
    return {
        "message": "Classes fetched successfully",
        "status": "success",
        "status_code": status.HTTP_201_CREATED,
        "data": classes
     }
    