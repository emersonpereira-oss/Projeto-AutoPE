from django.urls import path
from . import views

app_name = 'tentativas'

urlpatterns = [
    path('', views.lista_tentativas, name='lista'),
]
