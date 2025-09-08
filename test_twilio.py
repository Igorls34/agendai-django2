#!/usr/bin/env python
"""
Script para testar a integração com Twilio WhatsApp
Execute: python test_twilio.py
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

def test_twilio_whatsapp():
    """Testa o envio de WhatsApp via Twilio"""

    # Verificar configurações
    print("=== Verificando Configurações ===")
    print(f"TWILIO_ACCOUNT_SID: {settings.TWILIO_ACCOUNT_SID[:10]}...")
    print(f"TWILIO_WHATSAPP_NUMBER: {settings.TWILIO_WHATSAPP_NUMBER}")

    if not settings.TWILIO_ACCOUNT_SID or settings.TWILIO_ACCOUNT_SID == 'your_account_sid':
        print("❌ ERRO: TWILIO_ACCOUNT_SID não configurado!")
        return

    if not settings.TWILIO_AUTH_TOKEN or settings.TWILIO_AUTH_TOKEN == 'your_auth_token':
        print("❌ ERRO: TWILIO_AUTH_TOKEN não configurado!")
        return

    # Testar conexão
    print("\n=== Testando Conexão ===")
    try:
        client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
        account = client.api.accounts(settings.TWILIO_ACCOUNT_SID).fetch()
        print(f"✅ Conectado! Account: {account.friendly_name}")
    except Exception as e:
        print(f"❌ ERRO na conexão: {e}")
        return

    # Solicitar número para teste
    print("\n=== Teste de Envio ===")
    test_number = input("Digite seu número de WhatsApp (ex: 11999999999): ").strip()

    if not test_number:
        print("❌ Nenhum número informado")
        return

    # Formatar número
    test_number = ''.join(filter(str.isdigit, test_number))
    if not test_number.startswith('55'):
        test_number = f'55{test_number}'
    formatted_number = f'+{test_number}'

    print(f"Número formatado: {formatted_number}")

    # Enviar teste
    try:
        message = client.messages.create(
            body="🧪 Teste do AgendAI - WhatsApp funcionando!",
            from_=settings.TWILIO_WHATSAPP_NUMBER,
            to=f'whatsapp:{formatted_number}'
        )
        print(f"✅ Mensagem enviada! SID: {message.sid}")
        print(f"� Status da mensagem: {message.status}")
        print("�📱 Verifique seu WhatsApp!")
        
        # Aguardar um pouco e verificar status
        import time
        time.sleep(3)
        updated_message = client.messages(message.sid).fetch()
        print(f"📊 Status atualizado: {updated_message.status}")
        if updated_message.error_code:
            print(f"❌ Erro: {updated_message.error_message}")
    except Exception as e:
        print(f"❌ ERRO no envio: {e}")
        print(f"🔍 Detalhes do erro: {str(e)}")

if __name__ == '__main__':
    test_twilio_whatsapp()
