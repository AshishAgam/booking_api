from fastapi import FastAPI
from app.database import engine, Base
from app import models

import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# create all tables
Base.metadata.create_all(bind=engine)

from app.routes import classes, booking

app = FastAPI(title="Fitness Studio Booking API")

# Include Routers
app.include_router(classes.router)
app.include_router(booking.router)