from datetime import datetime, timedelta
from app.database import SessionLocal
from app.models import FitnessClassModel

db = SessionLocal()

sample_classes = [
    FitnessClassModel(name="Yoga", datetime=datetime.now() + timedelta(days=1), instructor="Anjali", available_slots=10),
    FitnessClassModel(name="Zumba", datetime=datetime.now() + timedelta(days=2), instructor="Rahul", available_slots=15),
    FitnessClassModel(name="HIIT", datetime=datetime.now() + timedelta(days=3), instructor="Priya", available_slots=12),
]

db.add_all(sample_classes)
db.commit()
db.close()

print("Seed data added!")
