from django.urls import path
from . import views

app_name = 'veiculos'

urlpatterns = [
    path('', views.lista_veiculos, name='lista'),
    path('<int:id>/', views.detalhe_veiculo, name='detalhe'),
]
