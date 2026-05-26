# 🎀 DIVI S KUMAR — 1st Birthday Digital Invitation

> **Live URL:** [divi-doll-birthday.pages.dev](https://divi-doll-birthday.pages.dev)  
> **Birthday:** Saturday, June 13, 2026 · 5:00 PM  
> **Venue:** Radiant Resort, Bannerghatta Road, Bengaluru  
> **Author:** Deepika Narendran (JoinDeeHub)

---

## ✨ What Was Built

A complete, fully live **digital birthday invitation** for Divi's 1st birthday.
No frameworks, no build tools — pure HTML/CSS/JS hosted on Cloudflare Pages with Supabase for real-time RSVP tracking.

---

## 🌐 Live Stack

| Layer | Technology | Details |
|-------|-----------|--------|
| **Frontend** | HTML / CSS / JS | Single `index.html` file |
| **Hosting** | Cloudflare Pages | Auto-deploys from `main` branch |
| **Database** | Supabase (PostgreSQL) | RSVPs, visitors, events |
| **Fonts** | Google Fonts | Cormorant Garamond, Montserrat, Great Vibes |
| **Repo** | GitHub — JoinDeeHub | `divi-birthday-invite` |

---

## 📱 5 Invitation Screens

| Screen | Content |
|--------|---------|
| 1 — Landing | Floating envelope animation, Divi's name, animated gold CTA |
| 2 — Invite Card | Luxury card with full invitation text |
| 3 — Party Details | Date, time, venue + live countdown timer to June 13 |
| 3b — Charity | Lunch at Shree Ramana Maharishi Academy for the Blind 🌟 |
| 4 — RSVP | Yes → name + adults + kids + food form; No → name prompt overlay |
| 5 — Thank You | Confetti, personalised message, WhatsApp share + copy link |

---

## 🎨 Visual Features

- 16 blush/champagne/gold balloons rising continuously
- Gold shimmer floating particles in background
- Animated gold CTA buttons with glow pulse
- Cormorant Garamond serif — luxury editorial font
- Rose-to-deep-plum countdown panel
- Smooth screen fade transitions with splash overlay
- Hover effects on all cards and buttons
- Mobile-first responsive design
- Double-tap photo reveal of Divi 📸

---

## 🗄️ Supabase Database Schema

### Tables

```sql
-- Track every visitor who opens the link
create table visitors (
  id            uuid primary key default gen_random_uuid(),
  session_id    text not null unique,
  referrer      text,
  device        text,
  ip_country    text,
  first_seen_at timestamptz default now(),
  last_seen_at  timestamptz default now()
);

-- Every RSVP submitted
create table rsvps (
  id           uuid primary key default gen_random_uuid(),
  session_id   text,
  name         text,
  attending    boolean not null,
  adults       int default 0,
  kids         int default 0,
  food         text,
  submitted_at timestamptz default now()
);

-- Every tap and interaction tracked
create table events (
  id           uuid primary key default gen_random_uuid(),
  session_id   text,
  event_name   text not null,
  screen       text,
  created_at   timestamptz default now()
);
```

### RLS Policies
- `anon` role → INSERT on all 3 tables + UPDATE on visitors
- `authenticated` role → SELECT on all 3 tables (for admin queries)

---

## 📊 RSVP Dashboard Queries

Run these in Supabase SQL Editor anytime:

```sql
-- All attending guests
select
  name as "Family / Guest",
  adults as "Adults",
  kids as "Kids",
  (adults + kids) as "Total People",
  food as "Food Preference",
  to_char(submitted_at at time zone 'Asia/Kolkata', 'DD Mon YYYY  HH12:MI AM') as "RSVP'd At"
from rsvps
where attending = true
order by submitted_at;

-- Headcount summary
select
  count(case when attending     then 1 end)              as "Yes RSVPs",
  count(case when not attending then 1 end)              as "No RSVPs",
  sum(case when attending then adults else 0 end)        as "Total Adults",
  sum(case when attending then kids   else 0 end)        as "Total Kids",
  sum(case when attending then adults + kids else 0 end) as "Grand Total Guests"
from rsvps;

-- Food breakdown for catering
select
  food as "Food Choice",
  count(*) as "Families",
  sum(adults + kids) as "Total Heads"
from rsvps
where attending = true
group by food
order by count(*) desc;

-- Full RSVP timeline (IST)
select
  to_char(submitted_at at time zone 'Asia/Kolkata', 'DD Mon  HH12:MI AM') as "Time",
  name as "Family",
  case when attending then 'Coming' else 'Declined' end as "Status"
from rsvps
order by submitted_at;
```

---

## 📂 Folder Structure

```
divi-birthday-invite/
├── frontend/
│   └── public/
│       ├── index.html        ← Complete invitation (single file)
│       └── DIVI_baby.jpeg    ← Divi's photo
├── supabase/
│   └── schema.sql        ← DB schema + RLS policies (idempotent)
└── README.md
```

---

## 🚀 Deployment

### Cloudflare Pages Setup
1. Connect GitHub repo `JoinDeeHub/divi-birthday-invite`
2. Build settings:
   - **Framework preset:** None
   - **Build command:** *(leave empty)*
   - **Output directory:** `frontend/public`
3. Every push to `main` → auto-deploys in ~30 seconds

### Supabase Setup
1. Create project at [supabase.com](https://supabase.com)
2. Run `supabase/schema.sql` in SQL Editor
3. Copy **Project URL** and **anon key**
4. Add to `index.html`:
```js
const SUPABASE_URL = 'https://your-project.supabase.co';
const SUPABASE_KEY = 'your-anon-key';
```

---

## 📲 WhatsApp Sharing

Send guests this message (works on all phones):

```
🎀✨ *A Special Invitation* ✨🎀

One year ago, our world became brighter
in the most beautiful way. 🌸

Now we would love to celebrate
*DIVI's very first birthday* with you! 💖

👑 *DIVI S KUMAR*
🎂 *Turns One — June 13, 2026*
🕔 *5:00 PM onwards*
📍 *Radiant Resort, Bengaluru*

Tap below to open your personal invitation 👇
🔗 https://divi-doll-birthday.pages.dev

*With love,*
*Dee's Family* 🤍
```

---

## 🔑 Environment Variables

No `.env` file needed — keys are embedded directly in `index.html` (Supabase anon key is safe to be public, protected by RLS policies).

---

## 📅 Event Details

| Detail | Info |
|--------|------|
| **Child** | DIVI S KUMAR |
| **Birthday** | June 13, 2026 |
| **Time** | 5:00 PM onwards |
| **Venue** | Radiant Resort |
| **Address** | C.K.Palya Road, 17th km, Bannerghatta Road, Bengaluru — 560083 |
| **RSVP Deadline** | June 5, 2026 |
| **Charity** | Lunch for children at Shree Ramana Maharishi Academy for the Blind, JP Nagar |

---

*Built with love 🤍 — [JoinDeeHub](https://github.com/JoinDeeHub) · by Divi's Mom*
