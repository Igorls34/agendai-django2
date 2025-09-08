#!/usr/bin/env python
"""
Script para testar email em produção
Execute: python test_email_prod.py
"""

import os
import sys
import django

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'agendai.settings')
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
django.setup()

from django.core.mail import send_mail

def test_email_production():
    """Testa envio de email em produção"""

    print("=== Teste de Email em Produção ===")

    try:
        send_mail(
            subject='Teste AgendAI - Produção',
            message='Este é um teste de email em produção do sistema AgendAI.',
            from_email='noreply@agendai.com',
            recipient_list=['igorlaurindo49@gmail.com'],
            fail_silently=False,
        )

        print("✅ Email enviado com sucesso para igorlaurindo49@gmail.com")
        print("📧 Verifique sua caixa de entrada!")

    except Exception as e:
        print(f"❌ Erro ao enviar email: {e}")
        print("🔧 Verifique as configurações de email no settings.py")

if __name__ == '__main__':
    test_email_production()
