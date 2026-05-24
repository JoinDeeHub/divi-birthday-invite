from flask import Blueprint, jsonify, request
from models.database import RSVP
import os

stats_bp = Blueprint('stats', __name__)

def require_admin(req):
    token = req.headers.get('X-Admin-Token', '')
    return token == os.environ.get('ADMIN_TOKEN', 'changeme')

@stats_bp.route('/stats', methods=['GET'])
def get_stats():
    if not require_admin(request):
        return jsonify({'error': 'Unauthorized'}), 401

    all_rsvps = RSVP.query.all()
    attending = [r for r in all_rsvps if r.attending]
    declined  = [r for r in all_rsvps if not r.attending]

    return jsonify({
        'total_invited':   RSVP.query.count(),
        'confirmed':       len(attending),
        'declined':        len(declined),
        'total_adults':    sum(r.adults for r in attending),
        'total_kids':      sum(r.kids   for r in attending),
        'food_veg':        sum(1 for r in attending if r.food_pref == 'veg'),
        'food_nonveg':     sum(1 for r in attending if r.food_pref == 'nonveg'),
        'food_both':       sum(1 for r in attending if r.food_pref == 'both'),
    })
