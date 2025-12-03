from django.urls import path
from . import views

app_name = 'clientes'

urlpatterns = [
    path('cadastro/', views.cadastro_cliente, name='cadastro_cliente'),
    path('login/', views.login_cliente, name='login_cliente'),
    path('perfil/', views.perfil_cliente, name='perfil_cliente'),
]
