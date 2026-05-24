# 🎀 DIVI S Kumar — 1st Birthday Digital Invitation

> **Birthday:** June 13, 2026  
> **Theme:** Elegant Pink — Soft Blush · Ivory White · Champagne Gold  
> **Author:** Deepika Narendran (DevOps / Full-Stack)

---

## Table of Contents

1. [What Was Built (Phase 1 — Complete)](#1-what-was-built)
2. [What Was Fixed](#2-what-was-fixed)
3. [Customization Guide](#3-customization-guide)
4. [Full Architecture](#4-full-architecture)
5. [Project Folder Structure](#5-folder-structure)
6. [Backend API — Flask](#6-backend-api)
7. [Database Schema](#7-database-schema)
8. [Admin Dashboard](#8-admin-dashboard)
9. [WhatsApp Automation](#9-whatsapp-automation)
10. [Deployment Guide](#10-deployment-guide)
11. [7-Day Build Plan](#11-7-day-build-plan)
12. [Future Ideas](#12-future-ideas)

---

## 1. What Was Built

### Phase 1 — `invite.html` (Delivered ✅)

A complete, self-contained, single HTML file digital birthday invitation.  
No framework, no server needed for basic use — open in any browser or host on any static server.

**5 interactive screens:**

| Screen | Content |
|--------|--------|
| 1 — Landing | Floating envelope, Divi's name, animated CTA button |
| 2 — Invite Card | Luxury card reveal with full invitation text |
| 3 — Details | Event date/time/venue + live countdown timer |
| 4 — RSVP | Yes/No choice → attending form (name, adults, kids, food) |
| 5 — Thank You | Confetti burst, personalised message, WhatsApp + copy link share |

**Visual features:**
- 16 blush/champagne/gold balloons rising continuously
- Gold shimmer floating particles in background
- Champagne gold animated CTA button
- Cormorant Garamond serif — luxury editorial font
- Rose-to-deep-plum countdown panel
- Smooth screen fade transitions
- Hover effects on all cards and buttons
- Mobile-first responsive design

---

## 2. What Was Fixed

| Bug | Root Cause | Fix Applied |
|-----|-----------|------------|
| "Open Invitation" button did nothing | `display:none` on screens wasn't being overridden cleanly in some browsers | Rewrote screen system to use `display:flex` toggled by `.active` class with `requestAnimationFrame` transition |
| Screen transition was jarring | No opacity transition between screens | Added fade in/out with opacity + `requestAnimationFrame` double-tick trick |
| Balloons appeared choppy | `animation-delay` was positive, so first run had blank start gap | Changed to negative delay (`delay = -(Math.random() * dur)`) so balloons start mid-animation immediately on load |
| Confetti lingered forever | No cleanup after animation | Added `setTimeout` to clear confetti DOM after 3.5s |
| Form reset broken when going back | RSVP form state not reset on back navigation | `resetInvite()` function resets all form fields and RSVP state |
| Select dropdown had no chevron | Browser default appearance removed without replacement | Added SVG chevron via `background-image` |

---

## 3. Customization Guide

Open `frontend/public/invite.html` in any text editor and update these values:

### Event Details (Screen 3)
```html
<!-- Line ~235 — Venue -->
<span class="d-value">Your Venue Name</span>
<span class="d-sub">City, India</span>
```

### RSVP Deadline (Screen 4)
```html
<!-- Line ~275 -->
<div class="rsvp-sub">✦ &nbsp; Kindly respond by June 1st &nbsp; ✦</div>
```

### Countdown Target Date & Time (JavaScript)
```js
// Line ~370
const target = new Date('2026-06-13T18:00:00+05:30').getTime();
//                       ─────────────── ────── ─────
//                       Date            Time   IST offset
```

### WhatsApp Share Message
```js
// Line ~400
const msg = encodeURIComponent(
  '🎀 You\'re invited to DIVI S Kumar\'s 1st Birthday!\n' +
  '📅 June 13, 2026  |  🕕 6:00 PM\n' +
  '✦ Join us for this precious milestone!\n\n' +
  'Open your invitation: https://divi.deehub.dev/invite'  // ← change URL
);
```

### Invite Link (Copy button)
```js
// Line ~395
const url = 'https://divi.deehub.dev/invite';  // ← change to your hosted URL
```

### Adding Divi's Photo
Inside `.invite-card` (Screen 2), after the `.one-ring` div, add:
```html
<img
  src="divi-photo.jpg"
  alt="Baby Divi"
  style="
    width: 120px;
    height: 120px;
    border-radius: 50%;
    object-fit: cover;
    border: 2px solid #c9a84c;
    box-shadow: 0 0 0 6px rgba(201,168,76,0.12);
    margin: 16px auto;
    display: block;
  "
/>
```

---

## 4. Full Architecture

```
┌──────────────────────────────────────────────────────┐
│                   GUEST                              │
│   Opens personalised URL:                            │
│   https://divi.deehub.dev/invite/sharma-family       │
└──────────────────┬───────────────────────────────────┘
                   │
                   ▼
┌──────────────────────────────────────────────────────┐
│   FRONTEND  (Vercel / Netlify — Free tier)           │
│   invite.html  OR  Next.js app                       │
│   • 5-screen animated invitation                     │
│   • Reads ?guest=sharma-family from URL              │
│   • Shows personalised greeting                      │
│   • POSTs RSVP to backend API                        │
└──────────────────┬───────────────────────────────────┘
                   │  POST /api/rsvp
                   ▼
┌──────────────────────────────────────────────────────┐
│   BACKEND  (Railway / Render — Free tier)            │
│   Flask or FastAPI                                   │
│   • /api/rsvp    — save RSVP to DB                  │
│   • /api/guests  — list all RSVPs (auth required)   │
│   • /api/stats   — counts for dashboard             │
└──────────────────┬───────────────────────────────────┘
                   │
                   ▼
┌──────────────────────────────────────────────────────┐
│   DATABASE  (Supabase / Postgres — Free tier)        │
│   tables: guests, rsvps                              │
└──────────────────────────────────────────────────────┘
                   │
                   ▼
┌──────────────────────────────────────────────────────┐
│   ADMIN DASHBOARD  (same frontend, /admin route)     │
│   • Total invited / confirmed / declined / pending   │
│   • Guest list with details                          │
│   • Food count breakdown                             │
│   • Kids count                                       │
│   • Export to CSV                                    │
└──────────────────────────────────────────────────────┘
```

---

## 5. Folder Structure

```
divi-birthday/
│
├── frontend/
│   ├── public/
│   │   └── invite.html              ← Phase 1 (done ✅)
│   ├── pages/
│   │   ├── index.js                 ← Landing / redirect
│   │   ├── invite/[guest].js        ← Personalised invite page
│   │   └── admin/
│   │       └── index.js             ← RSVP dashboard
│   ├── components/
│   │   ├── Balloons.jsx
│   │   ├── CountdownTimer.jsx
│   │   ├── InviteCard.jsx
│   │   ├── RSVPForm.jsx
│   │   └── SuccessScreen.jsx
│   ├── styles/
│   │   └── globals.css
│   └── next.config.js
│
├── backend/
│   ├── app.py                       ← Flask entry point
│   ├── routes/
│   │   ├── rsvp.py                  ← POST /api/rsvp
│   │   ├── guests.py                ← GET /api/guests
│   │   └── stats.py                 ← GET /api/stats
│   ├── models/
│   │   └── database.py              ← SQLAlchemy models
│   ├── utils/
│   │   └── whatsapp.py              ← WhatsApp message sender
│   └── requirements.txt
│
├── assets/
│   ├── photos/
│   │   └── divi-main.jpg
│   └── music/
│       └── lullaby-soft.mp3         ← Optional background music
│
├── docker-compose.yml
├── .env.example
└── README.md
```

---

## 6. Backend API

### `backend/app.py`
```python
from flask import Flask
from flask_cors import CORS
from routes.rsvp    import rsvp_bp
from routes.guests  import guests_bp
from routes.stats   import stats_bp
from models.database import db
import os

app = Flask(__name__)
CORS(app, origins=["https://divi.deehub.dev"])

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
app.config['SECRET_KEY']              = os.environ['SECRET_KEY']

db.init_app(app)

app.register_blueprint(rsvp_bp,    url_prefix='/api')
app.register_blueprint(guests_bp,  url_prefix='/api')
app.register_blueprint(stats_bp,   url_prefix='/api')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=False, port=5000)
```

### `backend/routes/rsvp.py`
```python
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

    existing = RSVP.query.filter_by(guest_key=data['guest_key']).first()
    if existing:
        rsvp = existing
    else:
        rsvp = RSVP()
        db.session.add(rsvp)

    rsvp.guest_key    = data['guest_key']
    rsvp.guest_name   = data.get('guest_name', '')
    rsvp.attending    = data['attending']
    rsvp.adults       = int(data.get('adults', 0))
    rsvp.kids         = int(data.get('kids', 0))
    rsvp.food_pref    = data.get('food_pref', '')
    rsvp.submitted_at = datetime.utcnow()

    db.session.commit()
    return jsonify({'status': 'ok', 'rsvp_id': rsvp.id}), 200
```

### `backend/routes/stats.py`
```python
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
```

---

## 7. Database Schema

### `backend/models/database.py`
```python
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Guest(db.Model):
    """Pre-loaded guest list — used to generate personalised links."""
    __tablename__ = 'guests'

    id          = db.Column(db.Integer, primary_key=True)
    key         = db.Column(db.String(80), unique=True, nullable=False)
    name        = db.Column(db.String(120), nullable=False)
    phone       = db.Column(db.String(20))
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
    submitted_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at   = db.Column(db.DateTime, onupdate=datetime.utcnow)
```

### Seed guests (run once)
```python
# seed_guests.py
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
```

---

## 8. Admin Dashboard

The admin dashboard lives at `/admin` (password protected). It shows:

```
┌──────────────────────────────────────────────────────┐
│  DIVI'S BIRTHDAY — RSVP DASHBOARD          June 2026 │
├──────────────┬─────────────┬──────────┬──────────────┤
│  Invited     │  Confirmed  │ Declined │  Pending     │
│     42       │     28      │    6     │     8        │
├──────────────┴─────────────┴──────────┴──────────────┤
│  Total Adults: 56   Total Kids: 14   Total Heads: 70 │
├──────────────────────────────────────────────────────┤
│  Food: Veg 24  Non-veg 18  Both 14                   │
├──────────────────────────────────────────────────────┤
│  GUEST LIST                                          │
│  Name              Adults Kids Food    Status        │
│  Sharma Family       2     1    Veg    ✅ Confirmed  │
│  Kumar Family        4     0    Both   ✅ Confirmed  │
│  Reddy Family        —     —    —      ⏳ Pending    │
└──────────────────────────────────────────────────────┘
```

Build it in 1 day with:
- React table with `useState` filtering
- Fetch from `/api/guests` with admin token header
- Export CSV button — `Papa.unparse()` from PapaParse
- Password gate using `localStorage` token

---

## 9. WhatsApp Automation

### `backend/utils/whatsapp.py`
```python
import requests
import os

WHATSAPP_TOKEN  = os.environ['WHATSAPP_TOKEN']
PHONE_NUMBER_ID = os.environ['WHATSAPP_PHONE_NUMBER_ID']

def send_invite(guest_name: str, guest_phone: str, guest_key: str):
    """Send personalised WhatsApp invite using Meta Business API."""
    invite_url = f"https://divi.deehub.dev/invite/{guest_key}"

    message = (
        f"🎀 Dear {guest_name},\n\n"
        f"DIVI S Kumar is turning ONE!\n"
        f"We'd love to celebrate this precious milestone with you.\n\n"
        f"📅 June 13, 2026  |  🕕 6:00 PM\n"
        f"📍 Your Venue, City\n\n"
        f"✦ Open your personal invitation:\n"
        f"{invite_url}\n\n"
        f"With love,\nDeepi & Family 💕"
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
```

### Send to all guests
```python
# send_invites.py
from app import app
from models.database import Guest
from utils.whatsapp import send_invite
import time

with app.app_context():
    guests = Guest.query.all()
    for g in guests:
        result = send_invite(g.name, g.phone, g.key)
        print(f"Sent to {g.name}: {result}")
        time.sleep(1)  # avoid rate limits
```

---

## 10. Deployment Guide

### Frontend — Vercel (free)
```bash
# 1. Push to GitHub
git init
git add .
git commit -m "Divi birthday invite v1"
git remote add origin https://github.com/JoinDeeHub/divi-birthday-invite.git
git push origin main

# 2. Go to vercel.com → New Project → Import GitHub repo
# 3. Set build: Next.js (auto-detected)
# 4. Add environment variables:
#    NEXT_PUBLIC_API_URL = https://divi-api.railway.app
# 5. Deploy
```

### Backend — Railway (free tier)
```bash
# 1. Go to railway.app → New Project → Deploy from GitHub
# 2. Select your backend folder
# 3. Add environment variables:
#    DATABASE_URL    = (auto-set by Railway Postgres plugin)
#    SECRET_KEY      = (python -c "import secrets; print(secrets.token_hex())")
#    ADMIN_TOKEN     = your-admin-password
#    WHATSAPP_TOKEN  = (from Meta Developer Console)
#    WHATSAPP_PHONE_NUMBER_ID = (from Meta Developer Console)
# 4. Add Postgres plugin → DATABASE_URL auto-injected
# 5. Deploy
```

### Quick free option (static only — no backend)
1. Go to [app.netlify.com/drop](https://app.netlify.com/drop)
2. Drag and drop `frontend/public/invite.html`
3. Get URL like `https://happy-divi-abc123.netlify.app`
4. Share instantly — done in 30 seconds ✅

### Custom Domain (optional)
- Buy `diviturnsone.in` on GoDaddy / Namecheap (~₹800/year)
- Point CNAME to Vercel URL
- SSL auto-managed by Vercel

---

## 11. 7-Day Build Plan

| Day | Task | Hours |
|-----|------|-------|
| 1 ✅ | `invite.html` — complete animated invite (done!) | 3h |
| 2 | Personalise: add venue, Divi's photo, final text | 1h |
| 3 | Flask backend — RSVP API + Postgres schema | 4h |
| 4 | Admin dashboard — React table + stats cards | 4h |
| 5 | Personalised URLs — `/invite/[guest-key]` | 2h |
| 6 | WhatsApp automation — send all invites | 2h |
| 7 | Deploy frontend (Vercel) + backend (Railway) + domain | 3h |
| **Total** | | **~19 hours** |

---

## 12. Future Ideas

### Emotional additions (make it unforgettable)

**Timeline of Divi's first year** — horizontal scroll section:
```
Month 1 → Month 3 → Month 6 → Month 9 → Month 12
"First smile" "First laugh" "First solid food" "First step" "Today!"
```

**Live photo wall** — guests upload photos during the party:
```
POST /api/photos  →  save to S3 / Supabase Storage
GET  /api/photos  →  guest gallery wall auto-refreshes every 5s
```

**QR code physical card:**
```python
import qrcode
qr = qrcode.make(f"https://divi.deehub.dev/invite/{guest_key}")
qr.save(f"qr-codes/{guest_key}.png")
```

**AI voice invite (advanced):** Use ElevenLabs API to generate personalised voice notes, send as WhatsApp audio.

### Make it a product
After this birthday, you have a fully built reusable invitation platform:
- RSVP backend + Admin dashboard + WhatsApp automation
- Package as **tinycelebrations.in** or **invitebydee.com**
- Charge ₹999–₹2999 per event 🚀

---

## Environment Variables Reference

```bash
# .env.example

# Backend
DATABASE_URL=postgresql://user:pass@host:5432/divi_db
SECRET_KEY=your-very-secret-key-here
ADMIN_TOKEN=your-admin-dashboard-password

# WhatsApp (Meta Business API)
WHATSAPP_TOKEN=EAAxxxxxx
WHATSAPP_PHONE_NUMBER_ID=1234567890

# Frontend (Next.js)
NEXT_PUBLIC_API_URL=https://your-backend.railway.app
NEXT_PUBLIC_INVITE_BASE_URL=https://divi.deehub.dev
```

---

## Requirements

```
# backend/requirements.txt
flask==3.0.0
flask-cors==4.0.0
flask-sqlalchemy==3.1.1
psycopg2-binary==2.9.9
python-dotenv==1.0.0
requests==2.31.0
qrcode[pil]==7.4.2
```

---

*Built with love for DIVI S Kumar's first birthday 🎀 June 13, 2026*
