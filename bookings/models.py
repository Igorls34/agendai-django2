from django.db import models
from django.utils import timezone

class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    duration_minutes = models.PositiveIntegerField(default=30)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Appointment(models.Model):
    class Status(models.TextChoices):
        PENDING = 'pending', 'Pendente'
        CONFIRMED = 'confirmed', 'Confirmado'
        CANCELED = 'canceled', 'Cancelado'

    service = models.ForeignKey(Service, on_delete=models.PROTECT, related_name='appointments')
    customer_name = models.CharField(max_length=120)
    customer_email = models.EmailField(blank=True)
    customer_phone = models.CharField(max_length=30, blank=True)
    notes = models.TextField(blank=True)
    starts_at = models.DateTimeField()
    ends_at = models.DateTimeField()
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.PENDING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-starts_at']
        indexes = [
            models.Index(fields=['starts_at']),
            models.Index(fields=['service', 'starts_at']),
        ]

    def __str__(self):
        return f"{self.service} — {self.customer_name} em {timezone.localtime(self.starts_at).strftime('%d/%m/%Y %H:%M')}"
