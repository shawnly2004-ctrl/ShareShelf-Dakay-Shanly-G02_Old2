-- Run ONCE in Supabase -> SQL Editor, and again after adding new tables/migrations.
--
-- Why: Supabase exposes the "public" schema through an auto-generated REST API
-- (the Data API). Tables created by Django migrations have Row Level Security (RLS)
-- OFF, so anyone holding your public "anon" key could read them -- including
-- accounts_user (emails and password hashes).
-- Enabling RLS with no policies blocks the REST API completely. Django is NOT
-- affected: it connects as the "postgres" role, which bypasses RLS.

DO $$
DECLARE r record;
BEGIN
  FOR r IN SELECT tablename FROM pg_tables WHERE schemaname = 'public' LOOP
    EXECUTE format('ALTER TABLE public.%I ENABLE ROW LEVEL SECURITY', r.tablename);
  END LOOP;
END $$;