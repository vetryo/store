import os
import threading
from django.core.wsgi import get_wsgi_application

# Set default Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'store_project.settings')

# Create WSGI application (must be defined before anything else)
application = get_wsgi_application()

# --- Temporary: auto-run migrations on Render startup ---
try:
    from django.core.management import call_command

    def run_migrations():
        try:
            call_command("migrate", interactive=False)
            print("✅ Database migrated successfully on Render startup.")
        except Exception as e:
            print("❌ Migration failed:", e)

    threading.Thread(target=run_migrations).start()
except Exception as e:
    print("Migration setup error:", e)


# --- Temporary: auto-create admin user if none exists ---
try:
    from django.contrib.auth import get_user_model

    def create_admin():
        User = get_user_model()
        if not User.objects.filter(is_superuser=True).exists():
            User.objects.create_superuser(
                username="admin",
                email="admin@example.com",
                password="admin12345"
            )
            print("✅ Default admin user created: admin / admin12345")

    threading.Thread(target=create_admin).start()
except Exception as e:
    print("Admin creation setup error:", e)
