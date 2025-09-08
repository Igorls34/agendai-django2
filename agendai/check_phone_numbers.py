#!/usr/bin/env python
"""
Script para verificar números de telefone disponíveis no Twilio
Execute: python check_phone_numbers.py
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

def check_phone_numbers():
    """Verifica números de telefone disponíveis no Twilio"""

    print("=== Verificando Números de Telefone ===")

    try:
        client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)

        # Buscar números de telefone
        incoming_phone_numbers = client.incoming_phone_numbers.list(limit=20)

        if not incoming_phone_numbers:
            print("❌ Nenhum número de telefone encontrado!")
            print("📋 Você precisa comprar um número no Twilio:")
            print("   1. Acesse: https://console.twilio.com/us1/develop/phone-numbers/manage/incoming")
            print("   2. Clique em 'Buy a Number'")
            print("   3. Escolha um número brasileiro (+55)")
            print("   4. Atualize TWILIO_PHONE_NUMBER no settings.py")
            return

        print("✅ Números encontrados:")
        for number in incoming_phone_numbers:
            print(f"   📞 {number.phone_number} - {number.friendly_name}")

        # Sugerir usar o primeiro número
        if incoming_phone_numbers:
            suggested = incoming_phone_numbers[0].phone_number
            print(f"\n💡 Sugiro usar: {suggested}")
            print("   Copie este número para TWILIO_PHONE_NUMBER no settings.py")

    except Exception as e:
        print(f"❌ ERRO: {e}")
