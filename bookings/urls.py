from django.urls import path
from . import views
from . import test_views

urlpatterns = [
    # URLs de teste para debug
    path('test/', test_views.test_view, name='test_view'),
    path('simple/', test_views.simple_home, name='simple_home'),
    
    # URLs normais
    path('', views.home, name='home'),
    path('servico/<int:service_id>/agendar/', views.schedule, name='schedule'),
    path('availability/', views.availability, name='availability'),
    path('sucesso/<int:appointment_id>/', views.success, name='booking_success'),
    # Dashboard leve
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/export.csv', views.export_csv, name='export_csv'),
    path('dashboard/<int:appointment_id>/<str:new_status>/', views.update_status, name='update_status'),
]
