# send_invites.py — run once to send WhatsApp invites to all guests
from app import app
from models.database import Guest
from utils.whatsapp import send_invite
import time

with app.app_context():
    guests = Guest.query.all()
    for g in guests:
        result = send_invite(g.name, g.phone, g.key)
        print(f"Sent to {g.name}: {result}")
        time.sleep(1)  # 1 second delay between messages to avoid rate limits
