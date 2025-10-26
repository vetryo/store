# --- Auto-migrate on startup (temporary for Render) ---
import threading, os
from django.core.management import call_command

def run_migrations():
    try:
        call_command("migrate", interactive=False)
        print("✅ Database migrated successfully.")
    except Exception as e:
        print("❌ Migration failed:", e)

# Run in a separate thread so it doesn't block startup
threading.Thread(target=run_migrations).start()
