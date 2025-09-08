#!/usr/bin/env python
"""
Script para testar notificações diretamente
Execute: python test_notifications.py
"""

import os
import sys
import django

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'agendai.settings')
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
django.setup()

from bookings.models import Appointment, Service
from bookings.views import send_notification

def test_notifications():
    """Testa as notificações diretamente"""

    print("=== Teste de Notificações ===")

    # Criar um agendamento de teste
    try:
        service = Service.objects.first()
        if not service:
            print("❌ Nenhum serviço encontrado. Execute: python manage.py seed_demo")
            return

        # Criar agendamento de teste
        from django.utils import timezone
        from datetime import datetime, timedelta

        starts_at = timezone.now() + timedelta(days=1)
        ends_at = starts_at + timedelta(minutes=30)

        appt = Appointment.objects.create(
            service=service,
            customer_name='Teste Notificação',
            customer_email='teste@notificacao.com',
            customer_phone='24998190280',
            notes='Teste de notificação',
            starts_at=starts_at,
            ends_at=ends_at,
            status=Appointment.Status.PENDING,
        )

        print(f"✅ Agendamento criado - ID: {appt.id}")

        # Testar notificação de agendamento
        print("\n🚀 Testando notificação de agendamento...")
        send_notification(appt, 'booking')

        # Testar notificação de confirmação
        print("\n🚀 Testando notificação de confirmação...")
        appt.status = Appointment.Status.CONFIRMED
        appt.save()
        send_notification(appt, 'confirmation')

        # Limpar agendamento de teste
        appt.delete()
        print("\n✅ Teste concluído!")

    except Exception as e:
        print(f"❌ ERRO: {e}")
        import traceback
        traceback.print_exc()

if __name__ == '__main__':
    test_notifications()
