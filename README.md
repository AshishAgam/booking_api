# booking_api

# Fitness Studio Booking API (FastAPI)

A simple API to view and book fitness classes like Yoga, Zumba, and HIIT.

# Tech Stack
- Python 3.13.3
- FastAPI
- SQLite (in-memory DB)
- SQLAlchemy + Pydantic
- Pytz for timezone handling

---

1. **Clone the repository**
```bash
git clone https://github.com/AshishAgam/booking_api.git
cd booking-api
```

2. **Create and activate virtual environment**
```bash
python -m venv venv
# Activate:
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate
```
3. **Install dependencies**
```bash
pip install -r requirements.txt
```
4. **Seed the database with sample data**
```bash
python seed_data.py
```

5. **Run the FastAPI server**
```bash
uvicorn app.main:app --reload
```

# Sample API Requests
1. **List Available Classes (with timezone support)**
<!-- Example using Postman: -->
```bash
http://localhost:8000/classes?tz=America/New_York
```
2. **Book a Class**
```bash
http://localhost:8000/booking
```
3. **View User Bookings**
```bash
http://localhost:8000/booking?email=ashish@gmail.com
```
