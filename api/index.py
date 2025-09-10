import os
import sys
import traceback
from pathlib import Path

print("🔄 Iniciando aplicação Vercel...")

try:
    # Add the project root to Python path
    current_dir = Path(__file__).resolve().parent
    project_root = current_dir.parent
    sys.path.insert(0, str(project_root))
    print(f"✅ Project root: {project_root}")

    # Set environment variables
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'agendai.settings')
    print("✅ Django settings configurado")

    # Import Django
    import django
    django.setup()
    print("✅ Django setup completo")

    # Test database connection
    from django.db import connection
    with connection.cursor() as cursor:
        cursor.execute("SELECT 1")
    print("✅ Conexão com banco OK")

    # Check if we have services
    from bookings.models import Service
    service_count = Service.objects.count()
    print(f"✅ Serviços no banco: {service_count}")

    # Import WSGI application
    from django.core.wsgi import get_wsgi_application
    application = get_wsgi_application()
    print("✅ WSGI application criada")

except Exception as e:
    print(f"❌ ERRO CRÍTICO: {e}")
    print("📋 Traceback completo:")
    traceback.print_exc()
    
    # Create a simple error application
    def error_application(environ, start_response):
        response_body = f'''
        <h1>Erro na Aplicação</h1>
        <p><strong>Erro:</strong> {str(e)}</p>
        <pre>{traceback.format_exc()}</pre>
        '''
        status = '500 Internal Server Error'
        headers = [('Content-Type', 'text/html')]
        start_response(status, headers)
        return [response_body.encode('utf-8')]
    
    application = error_application
