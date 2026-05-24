from flask import Blueprint, request, jsonify
from models.database import RSVP, Guest
import os

guests_bp = Blueprint('guests', __name__)

def require_admin(req):
    token = req.headers.get('X-Admin-Token', '')
    return token == os.environ.get('ADMIN_TOKEN', 'changeme')

@guests_bp.route('/guests', methods=['GET'])
def list_guests():
    if not require_admin(request):
        return jsonify({'error': 'Unauthorized'}), 401

    guests = Guest.query.all()
    result = []
    for g in guests:
        rsvp = RSVP.query.filter_by(guest_key=g.key).first()
        result.append({
            'key':        g.key,
            'name':       g.name,
            'phone':      g.phone,
            'attending':  rsvp.attending    if rsvp else None,
            'adults':     rsvp.adults       if rsvp else None,
            'kids':       rsvp.kids         if rsvp else None,
            'food_pref':  rsvp.food_pref    if rsvp else None,
            'submitted':  rsvp.submitted_at.isoformat() if rsvp and rsvp.submitted_at else None,
        })
    return jsonify(result), 200
