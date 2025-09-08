from datetime import datetime, time, timedelta
from django.utils import timezone
from django.db.models import Q
from .models import Appointment, Service

BUSINESS_HOURS = {
    'start_hour': 9,  # 09:00
    'end_hour': 18,  # 18:00 (último início pode ser antes conforme duração)
}

def _combine(date_obj, t: time, tz):
    dt_naive = datetime.combine(date_obj, t)
    return timezone.make_aware(dt_naive, tz)

def generate_daily_slots(service: Service, date_obj):
    """Gera horários livres (lista de strings HH:MM) para um serviço em uma data.
     Considera duração do serviço e bloqueia conflitos.
     """
    tz = timezone.get_current_timezone()
    duration = timedelta(minutes=service.duration_minutes)
    start_time = time(BUSINESS_HOURS['start_hour'], 0)
    end_time = time(BUSINESS_HOURS['end_hour'], 0)
    now = timezone.localtime()  # para bloquear horários passados no dia atual
    # Coleta compromissos existentes no dia selecionado
    day_start = _combine(date_obj, time.min, tz)
    day_end = _combine(date_obj, time.max, tz)
    existing = Appointment.objects.filter(
        service=service,
        status__in=[Appointment.Status.PENDING, Appointment.Status.CONFIRMED],
        starts_at__lt=day_end,
        ends_at__gt=day_start,
    ).values('starts_at', 'ends_at')
    # Lista de intervalos ocupados
    busy = [(timezone.localtime(e['starts_at']), timezone.localtime(e['ends_at'])) for e in existing]
    candidate = _combine(date_obj, start_time, tz)
    end_of_day = _combine(date_obj, end_time, tz)
    free_slots = []
    while candidate + duration <= end_of_day:
        # Se for hoje, não ofereça horários passados
        if candidate.date() == now.date() and candidate <= now:
            candidate += duration
            continue
        conflict = False
        for s, e in busy:
            # conflito se [candidate, candidate+duration) intersecta [s, e)
            if not (candidate + duration <= s or candidate >= e):
                conflict = True
                break
        if not conflict:
            free_slots.append(candidate.strftime('%H:%M'))
        candidate += duration
    return free_slots
