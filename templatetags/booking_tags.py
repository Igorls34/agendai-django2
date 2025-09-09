from django import template
from django.utils import timezone

register = template.Library()

@register.filter
def local(value):
    """Converte datetime para timezone local"""
    if value:
        return timezone.localtime(value)
    return value
