from datetime import date
from django.test import TestCase
from django.utils import timezone
from .models import Service, Appointment
from .services import generate_daily_slots

class AvailabilityTests(TestCase):
    def setUp(self):
        self.service = Service.objects.create(name='Teste', duration_minutes=30)

    def test_slots_generated(self):
        d = date.today() + timezone.timedelta(days=1)
        slots = generate_daily_slots(self.service, d)
        self.assertTrue(len(slots) > 0)

    def test_conflict(self):
        d = date.today() + timezone.timedelta(days=1)
        tz = timezone.get_current_timezone()
        from datetime import datetime
        starts = timezone.make_aware(datetime.combine(d, timezone.datetime.min.time().replace(hour=9)), tz)
        ends = starts + timezone.timedelta(minutes=self.service.duration_minutes)
        Appointment.objects.create(service=self.service, customer_name='X', starts_at=starts, ends_at=ends)
        slots = generate_daily_slots(self.service, d)
        self.assertNotIn('09:00', slots)
