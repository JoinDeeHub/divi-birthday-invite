# Supabase Setup for Divi Birthday Invite

## 1. Create a Free Project
1. Go to [https://supabase.com](https://supabase.com) and sign up
2. Click **New Project** → fill in name & password → choose region **South Asia (Mumbai)**
3. Wait ~2 minutes for it to spin up

## 2. Run the Schema
1. In your Supabase project, go to **SQL Editor**
2. Paste the contents of `schema.sql` and click **Run**
3. You should see 3 tables created: `visitors`, `rsvps`, `events`

## 3. Get Your Keys
1. Go to **Settings → API**
2. Copy your **Project URL** (looks like `https://xxxx.supabase.co`)
3. Copy your **anon public key** (safe to use in frontend)

## 4. Add Keys to Cloudflare Pages
1. Go to [Cloudflare Dashboard](https://dash.cloudflare.com) → Pages → `divi-doll-birthday`
2. **Settings → Environment Variables** → Add:
   - `SUPABASE_URL` = your project URL
   - `SUPABASE_ANON_KEY` = your anon key
3. Redeploy

> **OR** (simpler for a static site): just replace the two placeholder values directly in `index.html`:
> ```js
> const SUPABASE_URL  = 'https://YOUR_PROJECT.supabase.co';
> const SUPABASE_KEY  = 'YOUR_ANON_KEY';
> ```

## 5. View Your Data
- Go to **Table Editor** in Supabase to see all visitors, RSVPs and events in real time
- Use **SQL Editor** to run queries like:
```sql
-- Who is attending?
select name, adults, kids, food, submitted_at
from rsvps where attending = true order by submitted_at;

-- Who said no?
select name, submitted_at from rsvps where attending = false;

-- How many unique visitors?
select count(*) from visitors;

-- What screens did people visit most?
select screen, count(*) from events
where event_name = 'screen_view'
group by screen order by count desc;

-- Who shared on WhatsApp?
select v.session_id, v.first_seen_at
from events e join visitors v on e.session_id = v.session_id
where e.event_name = 'wa_share';
```

## Tables at a Glance

| Table | What it stores |
|-------|----------------|
| `visitors` | Every unique browser session that opened the invite |
| `rsvps` | RSVP form submissions (yes/no + details) |
| `events` | Every user action: screen views, button taps, shares, reveal |
