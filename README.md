# ShareShelf

A peer-to-peer lending library for everyday tools and equipment (IT317-G3, CIT-U).
Full-stack **Django** (templates for the frontend) + **PostgreSQL on Supabase**.

## Setup

See the sections below. Feature documentation is added as features are merged.

## 1. Set up Supabase (PostgreSQL)

1. Go to <https://supabase.com> -> **New project**. Pick a nearby region and set a **database password** (save it).
2. Click **Connect** -> **Connection string** -> **Session pooler** (IPv4 compatible).
3. Copy the URI (`postgresql://postgres.<project-ref>:[YOUR-PASSWORD]@aws-0-<region>.pooler.supabase.com:5432/postgres`)
   and replace `[YOUR-PASSWORD]` (URL-encode special characters, e.g. `@` -> `%40`).
4. Keep it private: it goes only in `.env`, which is git-ignored.

## 2. Run locally

```bash
python -m venv venv
venv\Scripts\activate            # macOS/Linux: source venv/bin/activate
pip install -r requirements.txt
copy .env.example .env           # macOS/Linux: cp .env.example .env
python manage.py migrate
python manage.py runserver
```