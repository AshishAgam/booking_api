from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List
from app.main import logger
from app.database import SessionLocal
from app.schemas import ResponseModel, BookingOut, BookingIn
from app.models import FitnessClassModel, BookingModel

router = APIRouter(prefix="/booking", tags=["Bookings"])

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=ResponseModel[BookingOut])
def book_class(request:BookingIn, db: Session = Depends(get_db)):
    """Book a spot in a fitness class if available."""
    fitness_class = db.query(FitnessClassModel).filter_by(id=request.class_id).first()

    if not fitness_class:
        logger.info(f"Class not fount with given ClassID {request.class_id}")
        raise HTTPException(status_code=404, detail="Class not found")
    
    if fitness_class.available_slots <= 0:
        logger.info("No slot available")
        raise HTTPException(status_code=400, detail="No available slots")
    
    # create booking
    booking = BookingModel(
        client_name = request.client_name,
        client_email = request.client_email,
        class_id = request.class_id
    )

    fitness_class.available_slots -= 1
    db.add(booking)
    db.commit()
    db.refresh(booking)

    logger.info(f"Booking request by {request.client_email} for class {request.class_id}")

    return{
        "message": "Booking Successfull",
        "status": "success",
        "status_code": 201,
        "data": booking
    }


@router.get("/", response_model=ResponseModel[List[BookingOut]])
def get_booking_by_email(email: str = Query(...), db: Session = Depends(get_db)):
    """Fetch all bookings made by a specific client using their email."""
    booking = db.query(BookingModel).filter_by(client_email=email).all()

    logger.info(f"Fetch all bookings made by {email}")

    return{
        "message": "Bookings fetched successfully",
        "status": "success",
        "status_code": 200,
        "data": booking
    }