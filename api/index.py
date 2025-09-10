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

# Import WSGI application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
