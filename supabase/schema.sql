-- ============================================================
-- DIVI BIRTHDAY INVITE — Supabase Schema
-- Run this in Supabase Dashboard > SQL Editor
-- ============================================================

-- 1. VISITORS — one row per browser session
create table if not exists visitors (
  id           uuid primary key default gen_random_uuid(),
  session_id   text not null unique,
  referrer     text,
  device       text,
  ip_country   text,
  first_seen_at timestamptz default now(),
  last_seen_at  timestamptz default now()
);

-- 2. RSVPS — one row per form submission
create table if not exists rsvps (
  id           uuid primary key default gen_random_uuid(),
  session_id   text,
  name         text,
  attending    boolean not null,
  adults       int default 0,
  kids         int default 0,
  food         text,
  submitted_at timestamptz default now()
);

-- 3. EVENTS — every user action
create table if not exists events (
  id           uuid primary key default gen_random_uuid(),
  session_id   text,
  event_name   text not null,
  screen       text,
  created_at   timestamptz default now()
);

-- ============================================================
-- Row Level Security — allow anonymous inserts (public invite site)
-- ============================================================
alter table visitors enable row level security;
alter table rsvps    enable row level security;
alter table events   enable row level security;

-- Allow anon inserts
create policy "anon insert visitors" on visitors for insert to anon with check (true);
create policy "anon insert rsvps"    on rsvps    for insert to anon with check (true);
create policy "anon insert events"   on events   for insert to anon with check (true);

-- Allow anon update visitors (to update last_seen_at)
create policy "anon update visitors" on visitors for update to anon using (true);

-- Allow authenticated reads (for you to view the dashboard)
create policy "auth select visitors" on visitors for select to authenticated using (true);
create policy "auth select rsvps"    on rsvps    for select to authenticated using (true);
create policy "auth select events"   on events   for select to authenticated using (true);
