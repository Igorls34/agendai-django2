from django.http import HttpResponse
from django.shortcuts import render
import traceback

def test_view(request):
    """View de teste para debug"""
    try:
        # Teste 1: Response simples
        if request.GET.get('simple'):
            return HttpResponse("✅ Django funcionando!")
        
        # Teste 2: Template básico
        if request.GET.get('template'):
            return render(request, 'base.html', {'test': True})
        
        # Teste 3: Models
        if request.GET.get('models'):
            from .models import Service
            services = Service.objects.all()
            return HttpResponse(f"✅ Serviços encontrados: {services.count()}")
        
        # Teste 4: View original
        from .views import home
        return home(request)
        
    except Exception as e:
        return HttpResponse(f"""
        <h1>❌ Erro de Debug</h1>
        <p><strong>Erro:</strong> {str(e)}</p>
        <pre>{traceback.format_exc()}</pre>
        """, status=500)
