# seed_guests.py — run once to populate guests table
from app import app
from models.database import db, Guest

GUEST_LIST = [
    {"key": "sharma-family",  "name": "Sharma Family",  "phone": "+919876543210"},
    {"key": "kumar-family",   "name": "Kumar Family",   "phone": "+919876543211"},
    {"key": "reddy-family",   "name": "Reddy Family",   "phone": "+919876543212"},
    # add all your guests here
]

with app.app_context():
    for g in GUEST_LIST:
        guest = Guest(**g)
        db.session.add(guest)
    db.session.commit()
    print(f"Seeded {len(GUEST_LIST)} guests.")
