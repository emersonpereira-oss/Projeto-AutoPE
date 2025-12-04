from django.urls import path
from . import views

app_name = 'clientes'

urlpatterns = [
    path('', views.index, name='index'),
    path('cadastro/', views.cadastro_cliente, name='cadastro'),
    path('login/', views.login_cliente, name='login'),
    path('perfil/', views.perfil_cliente, name='perfil'),
    path('logout/', views.logout_cliente, name='logout'),
]
