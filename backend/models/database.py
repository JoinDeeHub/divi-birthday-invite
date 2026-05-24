from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Guest(db.Model):
    """Pre-loaded guest list — used to generate personalised links."""
    __tablename__ = 'guests'

    id          = db.Column(db.Integer, primary_key=True)
    key         = db.Column(db.String(80), unique=True, nullable=False)
    # e.g. "sharma-family" → URL: /invite/sharma-family
    name        = db.Column(db.String(120), nullable=False)
    # Display name in invite: "Dear Sharma Family,"
    phone       = db.Column(db.String(20))
    # For WhatsApp automation
    created_at  = db.Column(db.DateTime, default=datetime.utcnow)

class RSVP(db.Model):
    """Submitted RSVP responses."""
    __tablename__ = 'rsvps'

    id           = db.Column(db.Integer, primary_key=True)
    guest_key    = db.Column(db.String(80), db.ForeignKey('guests.key'))
    guest_name   = db.Column(db.String(120))
    attending    = db.Column(db.Boolean, nullable=False)
    adults       = db.Column(db.Integer, default=0)
    kids         = db.Column(db.Integer, default=0)
    food_pref    = db.Column(db.String(20))
    # "veg" | "nonveg" | "both"
    submitted_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at   = db.Column(db.DateTime, onupdate=datetime.utcnow)
