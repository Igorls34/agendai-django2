from django.http import HttpResponse
import traceback

def test_view(request):
    """View de teste simples para debug"""
    try:
        return HttpResponse("✅ Django funcionando no Vercel!")
    except Exception as e:
        return HttpResponse(f"❌ Erro: {str(e)}", status=500)

def simple_home(request):
    """Home simplificada para teste"""
    try:
        return HttpResponse("""
        <h1>🎉 AgendAI Funcionando!</h1>
        <p>Sistema de agendamento online</p>
        <a href="/admin/">Admin</a>
        """)
    except Exception as e:
        return HttpResponse(f"❌ Erro na home: {str(e)}", status=500)
