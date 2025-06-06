from pydantic import BaseModel, EmailStr
from typing import Optional, Generic, TypeVar
from datetime import datetime

T = TypeVar('T')

# ResponseModel
class ResponseModel(BaseModel, Generic[T]):
    message: str
    status: str
    status_code: int
    data: Optional[T]

class FitnessClassOut(BaseModel):
    id: int
    name: str
    datetime: datetime
    instructor: str
    available_slots: int

    class Config:
        from_attributes = True
        
class BookingIn(BaseModel):
    class_id: int
    client_name: str
    client_email: EmailStr

class BookingOut(BaseModel):
    id: int
    class_id: int
    client_name: str
    client_email: EmailStr
    fitness_class: FitnessClassOut

    class Config:
        from_attributes = True