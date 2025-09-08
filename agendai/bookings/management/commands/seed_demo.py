from django.core.management.base import BaseCommand
from bookings.models import Service

class Command(BaseCommand):
    help = 'Cria serviços de demonstração'

    def handle(self, *args, **options):
        items = [
            ('Avaliação Inicial', 30, 0),
            ('Consulta Padrão', 45, 120),
            ('Sessão Avançada', 60, 200),
        ]
        for name, dur, price in items:
            Service.objects.get_or_create(name=name, defaults={
                'duration_minutes': dur,
                'price': price,
                'description': f'Serviço: {name}',
                'is_active': True,
            })
        self.stdout.write(self.style.SUCCESS('Serviços de demonstração criados/atualizados.'))
