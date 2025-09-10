import os
import sys
from pathlib import Path

# Add the project root to Python path
current_dir = Path(__file__).resolve().parent
project_root = current_dir.parent
sys.path.insert(0, str(project_root))

# Set environment variables
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'agendai.settings')

# Import Django
import django
django.setup()

# Auto-configure database on first run
try:
    from bookings.models import Service
    # Check if database is empty
    if not Service.objects.exists():
        print("🔄 Banco vazio, configurando automaticamente...")
        from django.core.management import execute_from_command_line
        execute_from_command_line(['manage.py', 'migrate'])
        execute_from_command_line(['manage.py', 'create_basic_services'])
        print("✅ Banco configurado!")
except Exception as e:
    print(f"⚠️ Aviso na configuração do banco: {e}")

# Import WSGI application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
