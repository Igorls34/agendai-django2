#!/usr/bin/env python
"""Script para inicializar o banco de dados no Vercel"""
import os
import sys
import django
from pathlib import Path

# Add the project root to Python path
current_dir = Path(__file__).resolve().parent
sys.path.insert(0, str(current_dir))

# Set environment variables
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'agendai.settings')

# Setup Django
django.setup()

from django.core.management import execute_from_command_line

def setup_database():
    """Configura o banco de dados e cria dados iniciais"""
    try:
        print("🔄 Executando migrações...")
        execute_from_command_line(['manage.py', 'migrate'])
        
        print("🔄 Criando serviços básicos...")
        execute_from_command_line(['manage.py', 'create_basic_services'])
        
        print("✅ Banco de dados configurado com sucesso!")
        
    except Exception as e:
        print(f"❌ Erro ao configurar banco: {e}")
        import traceback
        traceback.print_exc()

if __name__ == '__main__':
    setup_database()
