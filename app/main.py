from fastapi import FastAPI
from app.database import engine, Base
from app import models

# create all tables
Base.metadata.create_all(bind=engine)

from app.routes import classes, booking

app = FastAPI(title="Fitness Studio Booking API")

# Include Routers
app.include_router(classes.router)
app.include_router(booking.router)