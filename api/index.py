import os
import sys
import django
from django.core.wsgi import get_wsgi_application

# Add the project directory to the Python path
sys.path.insert(0, os.path.dirname(__file__))

# Configure Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'agendai.settings')

# Setup Django
django.setup()

# Get the WSGI application
app = get_wsgi_application()

# Vercel expects the app to be named 'app'
application = app
