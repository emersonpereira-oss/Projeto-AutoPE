from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render

def dashboard(request):
    return render(request, 'dashboard/dashboard.html')

urlpatterns = [
    path('', dashboard, name='dashboard'),

    path('clientes/', include('clientes.urls')),
    path('veiculos/', include('veiculos.urls')),
    path('locacao/', include('locacao.urls')),
    path('pagamentos/', include('pagamentos.urls')),
    path('tentativas/', include('tentativas.urls')),
]
