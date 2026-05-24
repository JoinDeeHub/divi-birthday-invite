import requests
import os

WHATSAPP_TOKEN  = os.environ['WHATSAPP_TOKEN']
PHONE_NUMBER_ID = os.environ['WHATSAPP_PHONE_NUMBER_ID']

def send_invite(guest_name: str, guest_phone: str, guest_key: str):
    """Send personalised WhatsApp invite using Meta Business API."""
    invite_url = f"https://divi.deehub.dev/invite/{guest_key}"

    message = (
        f"\U0001f380 Dear {guest_name},\n\n"
        f"DIVI S Kumar is turning ONE!\n"
        f"We\u2019d love to celebrate this precious milestone with you.\n\n"
        f"\U0001f4c5 June 13, 2026  |  \U0001f555 6:00 PM\n"
        f"\U0001f4cd Your Venue, City\n\n"
        f"\u2726 Open your personal invitation:\n"
        f"{invite_url}\n\n"
        f"With love,\nDeepi & Family \U0001f495"
    )

    payload = {
        "messaging_product": "whatsapp",
        "to": guest_phone,
        "type": "text",
        "text": {"body": message}
    }

    response = requests.post(
        f"https://graph.facebook.com/v18.0/{PHONE_NUMBER_ID}/messages",
        headers={
            "Authorization": f"Bearer {WHATSAPP_TOKEN}",
            "Content-Type":  "application/json"
        },
        json=payload
    )
    return response.json()
