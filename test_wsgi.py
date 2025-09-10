#!/usr/bin/env python
"""Teste do WSGI para verificar se a aplicação carrega corretamente"""
import os
import sys
import django
from django.core.wsgi import get_wsgi_application

# Add the project directory to the Python path
project_dir = os.path.dirname(__file__)
sys.path.insert(0, project_dir)

# Configure Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'agendai.settings')

try:
    # Setup Django
    django.setup()
    print("✅ Django setup OK")

    # Get the WSGI application
    app = get_wsgi_application()
    print("✅ WSGI application OK")
    
    print("🎉 Tudo funcionando corretamente!")
    
except Exception as e:
    print(f"❌ Erro: {e}")
    import traceback
    traceback.print_exc()
