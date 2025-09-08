from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('servico/<int:service_id>/agendar/', views.schedule, name='schedule'),
    path('availability/', views.availability, name='availability'),
    path('sucesso/<int:appointment_id>/', views.success, name='booking_success'),
    # Dashboard leve
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/export.csv', views.export_csv, name='export_csv'),
    path('dashboard/<int:appointment_id>/<str:new_status>/', views.update_status, name='update_status'),
]
