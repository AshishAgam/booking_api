import pytz
from pytz import timezone as pytz_timezone
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional
from starlette import status
from app.main import logger
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
def get_classes(tz: Optional[str] = None, db: Session = Depends(get_db)):
    """Fetch all upcoming fitness classes."""
    classes = db.query(FitnessClassModel).all()

    ist = pytz.timezone("Asia/Kolkata")

    # If timezone param is passed, convert datetimes
    if tz:
        try:
            target_tz = pytz_timezone(tz)
            for c in classes:
                # convert IST to target timezone
                ist_dt = ist.localize(c.datetime)
                c.datetime = ist_dt.astimezone(target_tz)
        except Exception:
            logger.error(f"{tz} is invalid timezone string")
            raise HTTPException(status_code=400, detail="Invalid timezone string")
    
    logger.info("Fetched all upcoming classes successfully")

    return {
        "message": "Classes fetched successfully",
        "status": "success",
        "status_code": status.HTTP_201_CREATED,
        "data": classes
     }
    