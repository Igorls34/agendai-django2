#!/usr/bin/env python
"""
Script para testar SMS via Twilio
Execute: python test_sms.py
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

def test_sms():
    """Testa o envio de SMS via Twilio"""

    print("=== Testando SMS ===")
    print(f"Número Twilio: {settings.TWILIO_PHONE_NUMBER}")

    # Verificar configurações
    if not settings.TWILIO_ACCOUNT_SID or settings.TWILIO_ACCOUNT_SID == 'your_account_sid':
        print("❌ ERRO: TWILIO_ACCOUNT_SID não configurado!")
        return

    if not settings.TWILIO_AUTH_TOKEN or settings.TWILIO_AUTH_TOKEN == 'your_auth_token':
        print("❌ ERRO: TWILIO_AUTH_TOKEN não configurado!")
        return

    # Solicitar número para teste
    test_number = input("Digite seu número para teste (ex: 11999999999): ").strip()

    if not test_number:
        print("❌ Nenhum número informado")
        return

    # Formatar número
    test_number = ''.join(filter(str.isdigit, test_number))
    if not test_number.startswith('55'):
        test_number = f'55{test_number}'
    formatted_number = f'+{test_number}'

    print(f"Número formatado: {formatted_number}")

    # Enviar SMS
    try:
        client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)

        message = client.messages.create(
            body="🧪 Teste do AgendAI - SMS funcionando! Você receberá notificações de agendamento por aqui.",
            from_=settings.TWILIO_PHONE_NUMBER,
            to=formatted_number
        )
        print(f"✅ SMS enviado! SID: {message.sid}")
        print(f"📊 Status: {message.status}")
        print("📱 Verifique seu celular!")

        # Aguardar um pouco e verificar status
        import time
        time.sleep(5)
        updated_message = client.messages(message.sid).fetch()
        print(f"📊 Status atualizado: {updated_message.status}")
        if updated_message.error_code:
            print(f"❌ Erro: {updated_message.error_message}")

    except Exception as e:
        print(f"❌ ERRO no envio: {e}")
        print(f"🔍 Detalhes: {str(e)}")

if __name__ == '__main__':
    test_sms()
