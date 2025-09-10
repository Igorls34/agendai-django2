from django.core.management.base import BaseCommand
from bookings.models import Service

class Command(BaseCommand):
    help = 'Cria serviços básicos para teste'

    def handle(self, *args, **options):
        # Limpa serviços existentes
        Service.objects.all().delete()
        
        # Cria serviços básicos
        services_data = [
            {
                'name': 'Corte Masculino',
                'description': 'Corte de cabelo masculino tradicional',
                'duration_minutes': 30,
                'price': 25.00
            },
            {
                'name': 'Corte Feminino',
                'description': 'Corte de cabelo feminino',
                'duration_minutes': 45,
                'price': 40.00
            },
            {
                'name': 'Barba',
                'description': 'Aparar e fazer a barba',
                'duration_minutes': 20,
                'price': 15.00
            },
        ]
        
        for service_data in services_data:
            service = Service.objects.create(**service_data)
            self.stdout.write(
                self.style.SUCCESS(f'✅ Serviço criado: {service.name}')
            )
        
        self.stdout.write(
            self.style.SUCCESS(f'🎉 {len(services_data)} serviços criados com sucesso!')
        )
