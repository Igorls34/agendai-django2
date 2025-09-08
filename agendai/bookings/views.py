from datetime import datetime
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.db.models import Q
from django.http import JsonResponse, HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.utils import timezone
from twilio.rest import Client

from .forms import BookingForm
from .models import Appointment, Service
from .services import generate_daily_slots

def send_notification(appt, notification_type='booking'):
    """Envia notificações por email e SMS"""
    print(f"🔄 Enviando notificação do tipo: {notification_type}")
    print(f"👤 Cliente: {appt.customer_name}")
    print(f"📧 Email: {appt.customer_email}")
    print(f"📱 Telefone: {appt.customer_phone}")
    
    if notification_type == 'booking':
        subject = f'Novo Agendamento - {appt.service.name}'
        message = f'''
Olá {appt.customer_name},

Seu agendamento foi realizado com sucesso!

Detalhes:
- Serviço: {appt.service.name}
- Data/Hora: {appt.starts_at.strftime('%d/%m/%Y %H:%M')}
- Status: Pendente (aguardando confirmação)

Entraremos em contato em breve para confirmar.

Atenciosamente,
Equipe AgendAI
        '''.strip()
    else:  # confirmation
        subject = f'Confirmação de Agendamento - {appt.service.name}'
        message = f'''
Olá {appt.customer_name},

Seu agendamento foi confirmado!

Detalhes:
- Serviço: {appt.service.name}
- Data/Hora: {appt.starts_at.strftime('%d/%m/%Y %H:%M')}
- Status: Confirmado

Obrigado por escolher nossos serviços!

Atenciosamente,
Equipe AgendAI
        '''.strip()
    
    # 1. Enviar Email
    from_email = 'noreply@agendai.com'
    recipient_list = [appt.customer_email]
    
    try:
        send_mail(subject, message, from_email, recipient_list)
        print(f'✅ Email enviado para {appt.customer_email}')
    except Exception as e:
        print(f'❌ Erro ao enviar email: {e}')
    
    # 2. Enviar SMS (mais fácil que WhatsApp)
    if appt.customer_phone:
        print(f"📱 Telefone encontrado: {appt.customer_phone}")
        try:
            from django.conf import settings
            client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
            
            # Formatar número do telefone
            phone_number = appt.customer_phone.strip()
            print(f"📱 Telefone após strip: {phone_number}")
            
            # Remover caracteres não numéricos
            phone_number = ''.join(filter(str.isdigit, phone_number))
            print(f"📱 Telefone apenas números: {phone_number}")
            
            # Adicionar código do país se não tiver
            if not phone_number.startswith('55'):
                phone_number = f'55{phone_number}'
                print(f"📱 Adicionado código país: {phone_number}")
            
            # Garantir formato internacional
            if not phone_number.startswith('+'):
                phone_number = f'+{phone_number}'
                print(f"📱 Formato internacional: {phone_number}")
            
            print(f'🚀 Tentando enviar SMS para: {phone_number}')
            
            # Usar SMS em vez de WhatsApp (mais confiável)
            sms_message = client.messages.create(
                body=message,
                from_=settings.TWILIO_PHONE_NUMBER,  # Número do Twilio para SMS
                to=phone_number
            )
            print(f'✅ SMS enviado com sucesso! SID: {sms_message.sid}')
        except Exception as e:
            print(f'❌ Erro ao enviar SMS: {e}')
            print(f'🔍 Detalhes do erro: {str(e)}')
    else:
        print("❌ Nenhum telefone fornecido")

def home(request):
    services = Service.objects.filter(is_active=True).order_by('name')
    return render(request, 'bookings/home.html', {'services': services})

def schedule(request, service_id):
    print(f"🔄 VIEW SCHEDULE chamada - Service ID: {service_id}")
    service = get_object_or_404(Service, pk=service_id, is_active=True)
    if request.method == 'POST':
        print("📝 Método POST detectado")
        form = BookingForm(request.POST, service=service)
        if form.is_valid():
            print("✅ Formulário válido")
            date_str = form.cleaned_data['date'].strftime('%Y-%m-%d')
            time_str = form.cleaned_data['time'].strftime('%H:%M')
            tz = timezone.get_current_timezone()
            starts_at = timezone.make_aware(datetime.strptime(f"{date_str} {time_str}", '%Y-%m-%d %H:%M'), tz)
            ends_at = starts_at + timezone.timedelta(minutes=service.duration_minutes)
            # Confere disponibilidade no momento do POST
            available = generate_daily_slots(service, form.cleaned_data['date'])
            if time_str not in available:
                form.add_error('time', 'Este horário acabou de ser reservado. Escolha outro.')
            else:
                print(f"📝 Criando agendamento para: {form.cleaned_data['customer_name']}")
                print(f"📧 Email: {form.cleaned_data['customer_email']}")
                print(f"📱 Telefone: {form.cleaned_data['customer_phone']}")
                
                appt = Appointment.objects.create(
                    service=service,
                    customer_name=form.cleaned_data['customer_name'],
                    customer_email=form.cleaned_data['customer_email'],
                    customer_phone=form.cleaned_data['customer_phone'],
                    notes=form.cleaned_data['notes'],
                    starts_at=starts_at,
                    ends_at=ends_at,
                    status=Appointment.Status.PENDING,
                )
                
                print(f"✅ Agendamento criado - ID: {appt.id}")
                # Enviar notificação de agendamento
                print("🚀 Enviando notificação de agendamento...")
                send_notification(appt, 'booking')
                
                return redirect('booking_success', appointment_id=appt.id)
        else:
            print("❌ Formulário inválido")
            print(f"Erros: {form.errors}")
    else:
        print("📄 Método GET detectado")
        form = BookingForm(service=service)
    return render(request, 'bookings/schedule.html', {
        'service': service,
        'form': form,
    })

def availability(request):
    """Endpoint JSON para buscar horários disponíveis de um serviço numa data."""
    service_id = request.GET.get('service')
    date_str = request.GET.get('date')
    service = get_object_or_404(Service, pk=service_id, is_active=True)
    try:
        date_obj = datetime.strptime(date_str, '%Y-%m-%d').date()
    except Exception:
        return JsonResponse({'error': 'Data inválida.'}, status=400)
    slots = generate_daily_slots(service, date_obj)
    return JsonResponse({'service': service.name, 'date': date_str, 'slots': slots})

def success(request, appointment_id):
    appt = get_object_or_404(Appointment, pk=appointment_id)
    return render(request, 'bookings/success.html', {'appt': appt})

# --- Dashboard leve (para operar sem entrar no Django Admin) ---
@staff_member_required
def dashboard(request):
    services = Service.objects.all().order_by('name')
    q = request.GET.get('q', '').strip()
    status = request.GET.get('status', '')
    service_id = request.GET.get('service', '')
    date_from = request.GET.get('from', '')
    date_to = request.GET.get('to', '')
    appts = Appointment.objects.select_related('service').all()
    if q:
        appts = appts.filter(Q(customer_name__icontains=q) | Q(customer_email__icontains=q) | Q(customer_phone__icontains=q))
    if status:
        appts = appts.filter(status=status)
    if service_id:
        appts = appts.filter(service_id=service_id)
    if date_from:
        try:
            dt_from = timezone.make_aware(datetime.strptime(date_from + ' 00:00', '%Y-%m-%d %H:%M'))
            appts = appts.filter(starts_at__gte=dt_from)
        except Exception:
            pass
    if date_to:
        try:
            dt_to = timezone.make_aware(datetime.strptime(date_to + ' 23:59', '%Y-%m-%d %H:%M'))
            appts = appts.filter(starts_at__lte=dt_to)
        except Exception:
            pass
    appts = appts.order_by('starts_at')
    return render(request, 'bookings/dashboard.html', {
        'services': services,
        'appts': appts,
        'params': {
            'q': q,
            'status': status,
            'service': service_id,
            'from': date_from,
            'to': date_to,
        }
    })

@staff_member_required
def export_csv(request):
    import csv
    response = HttpResponse(content_type='text/csv; charset=utf-8')
    response['Content-Disposition'] = 'attachment; filename="agendai_appointments.csv"'
    writer = csv.writer(response)
    writer.writerow(['Serviço', 'Cliente', 'Email', 'Telefone', 'Início', 'Fim', 'Status', 'Criado em'])
    # Reuso dos filtros do dashboard
    request.GET = request.GET.copy()
    appts_view = dashboard  # truque para compartilhar lógica? melhor replicar filtros
    q = request.GET.get('q', '').strip()
    status = request.GET.get('status', '')
    service_id = request.GET.get('service', '')
    date_from = request.GET.get('from', '')
    date_to = request.GET.get('to', '')
    appts = Appointment.objects.select_related('service').all()
    if q:
        appts = appts.filter(Q(customer_name__icontains=q) | Q(customer_email__icontains=q) | Q(customer_phone__icontains=q))
    if status:
        appts = appts.filter(status=status)
    if service_id:
        appts = appts.filter(service_id=service_id)
    if date_from:
        try:
            dt_from = timezone.make_aware(datetime.strptime(date_from + ' 00:00', '%Y-%m-%d %H:%M'))
            appts = appts.filter(starts_at__gte=dt_from)
        except Exception:
            pass
    if date_to:
        try:
            dt_to = timezone.make_aware(datetime.strptime(date_to + ' 23:59', '%Y-%m-%d %H:%M'))
            appts = appts.filter(starts_at__lte=dt_to)
        except Exception:
            pass
    for a in appts.order_by('starts_at'):
        writer.writerow([
            a.service.name,
            a.customer_name,
            a.customer_email,
            a.customer_phone,
            timezone.localtime(a.starts_at).strftime('%d/%m/%Y %H:%M'),
            timezone.localtime(a.ends_at).strftime('%d/%m/%Y %H:%M'),
            a.get_status_display(),
            timezone.localtime(a.created_at).strftime('%d/%m/%Y %H:%M'),
        ])
    return response

@staff_member_required
def update_status(request, appointment_id, new_status):
    print(f"🔄 VIEW UPDATE_STATUS chamada - ID: {appointment_id}, Status: {new_status}")
    appt = get_object_or_404(Appointment, pk=appointment_id)
    print(f"📅 Agendamento encontrado: {appt.customer_name} - {appt.service.name}")
    
    if new_status not in dict(Appointment.Status.choices):
        print(f"❌ Status inválido: {new_status}")
        return redirect('dashboard')
    
    appt.status = new_status
    appt.save(update_fields=['status', 'updated_at'])
    print(f"✅ Status atualizado para: {new_status}")
    
    # Enviar notificações quando confirmado
    if new_status == 'confirmed':
        print("🚀 Enviando notificação de confirmação...")
        send_notification(appt, 'confirmation')
    else:
        print(f"ℹ️ Status {new_status} - nenhuma notificação enviada")
    
    return redirect('dashboard')
