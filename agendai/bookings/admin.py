from django.contrib import admin
from .models import Service, Appointment

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'duration_minutes', 'price', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('name', 'description')

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('service', 'customer_name', 'starts_at', 'ends_at', 'status')
    list_filter = ('status', 'service')
    search_fields = ('customer_name', 'customer_email', 'customer_phone')
    ordering = ('-starts_at',)
