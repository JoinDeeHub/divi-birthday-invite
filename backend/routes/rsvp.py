from flask import Blueprint, request, jsonify
from models.database import db, RSVP
from datetime import datetime

rsvp_bp = Blueprint('rsvp', __name__)

@rsvp_bp.route('/rsvp', methods=['POST'])
def submit_rsvp():
    data = request.get_json()

    required = ['guest_key', 'attending']
    if not all(k in data for k in required):
        return jsonify({'error': 'Missing fields'}), 400

    # Upsert — guest can update their RSVP
    existing = RSVP.query.filter_by(guest_key=data['guest_key']).first()
    if existing:
        rsvp = existing
    else:
        rsvp = RSVP()
        db.session.add(rsvp)

    rsvp.guest_key    = data['guest_key']
    rsvp.guest_name   = data.get('guest_name', '')
    rsvp.attending    = data['attending']           # True / False
    rsvp.adults       = int(data.get('adults', 0))
    rsvp.kids         = int(data.get('kids', 0))
    rsvp.food_pref    = data.get('food_pref', '')
    rsvp.submitted_at = datetime.utcnow()

    db.session.commit()
    return jsonify({'status': 'ok', 'rsvp_id': rsvp.id}), 200
