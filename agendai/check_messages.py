#!/usr/bin/env python
"""
Script para verificar mensagens do Twilio
Execute: python check_messages.py
"""

import os
import sys
import django

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'agendai.settings')
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
django.setup()

from django.conf import settings
from twilio.rest import Client

def check_messages():
    """Verifica as últimas mensagens enviadas"""

    print("=== Verificando Mensagens Recentes ===")

    try:
        client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)

        # Buscar mensagens recentes
        messages = client.messages.list(limit=5)

        for msg in messages:
            print(f"\n📨 SID: {msg.sid}")
            print(f"📞 Para: {msg.to}")
            print(f"📊 Status: {msg.status}")
            print(f"📅 Data: {msg.date_created}")
            if msg.error_code:
                print(f"❌ Erro: {msg.error_message}")
            print(f"💬 Mensagem: {msg.body[:50]}...")

    except Exception as e:
        print(f"❌ ERRO: {e}")

if __name__ == '__main__':
    check_messages()
