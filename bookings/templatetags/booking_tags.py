from django import template
from django.utils import timezone

register = template.Library()

@register.filter
def local(dt):
    try:
        return timezone.localtime(dt)
    except Exception:
        return dt
