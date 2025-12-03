from django.urls import path
from . import views

app_name = 'pagamentos'

urlpatterns = [
    path('', views.lista_pagamentos, name='lista'),
    path('novo/', views.novo_pagamento, name='novo'),
]
