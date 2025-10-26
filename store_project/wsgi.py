import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'store_project.settings')
application = get_wsgi_application()

# --- Temporary: run migrations automatically on Render startup ---
try:
    from django.core.management import call_command
    import threading

    def run_migrations():
        try:
            call_command("migrate", interactive=False)
            print("✅ Database migrated successfully on Render startup.")
        except Exception as e:
            print("❌ Migration failed:", e)

    threading.Thread(target=run_migrations).start()
except Exception as e:
    print("Migration setup error:", e)
