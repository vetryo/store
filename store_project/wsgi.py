import os
import threading
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'store_project.settings')
application = get_wsgi_application()

# --- Run migrations automatically ---
from django.core.management import call_command
def run_migrations():
    try:
        call_command("migrate", interactive=False)
        print("✅ Database migrated.")
    except Exception as e:
        print("❌ Migration error:", e)

threading.Thread(target=run_migrations).start()

# --- Ensure a superuser exists ---
from django.contrib.auth import get_user_model
def ensure_admin():
    User = get_user_model()
    if not User.objects.filter(is_superuser=True).exists():
        User.objects.create_superuser(
            username="qadyrbek",
            email="qadyrbek@example.com",
            password="Qadyrbek12345"
        )
        print("✅ Superuser created: qadyrbek / Qadyrbek12345")

threading.Thread(target=ensure_admin).start()
