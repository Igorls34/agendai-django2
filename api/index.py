import os

# Usar valor encontrado no manage.py
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "agendai.settings")

from django.core.wsgi import get_wsgi_application
app = get_wsgi_application()
