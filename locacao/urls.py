from django.urls import path
from . import views

app_name = 'locacao'

urlpatterns = [
    path('', views.lista_locacoes, name='lista'),
    path('nova/', views.nova_locacao, name='nova'),
    path('<int:id>/', views.detalhe_locacao, name='detalhe'),
]
