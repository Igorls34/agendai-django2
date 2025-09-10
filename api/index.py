import os
import sys
import traceback
from pathlib import Path

# Add project root to path
current_dir = Path(__file__).resolve().parent
project_root = current_dir.parent
sys.path.insert(0, str(project_root))

# Set Django settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "agendai.settings")

try:
    # Try to initialize Django
    import django
    django.setup()
    
    from django.core.wsgi import get_wsgi_application
    app = get_wsgi_application()
    
except Exception as e:
    # Create error handler if Django fails to initialize
    def error_app(environ, start_response):
        error_msg = f"""
        <html>
        <head><title>Django Initialization Error</title></head>
        <body>
        <h1>🚨 Django Initialization Error</h1>
        <h2>Error: {str(e)}</h2>
        <h3>Environment Variables:</h3>
        <ul>
        <li>SECRET_KEY: {"✅ Set" if os.getenv("SECRET_KEY") else "❌ Missing"}</li>
        <li>DEBUG: {os.getenv("DEBUG", "Not set")}</li>
        <li>DATABASE_URL: {"✅ Set" if os.getenv("DATABASE_URL") else "❌ Missing (using SQLite fallback)"}</li>
        <li>Python Path: {sys.path}</li>
        </ul>
        <h3>Full Traceback:</h3>
        <pre>{traceback.format_exc()}</pre>
        </body>
        </html>
        """
        status = '500 Internal Server Error'
        headers = [('Content-Type', 'text/html')]
        start_response(status, headers)
        return [error_msg.encode('utf-8')]
    
    app = error_app
