from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import render

def dashboard(request):
    return render(request, 'dashboard/dashboard.html')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', dashboard, name='dashboard'),

    path('clientes/', include('clientes.urls', namespace='clientes')),
    path('veiculos/', include('veiculos.urls', namespace='veiculos')),
    path('locacao/', include('locacao.urls', namespace='locacao')),
    path('pagamentos/', include('pagamentos.urls', namespace='pagamentos')),
    path('tentativas/', include('tentativas.urls', namespace='tentativas')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
