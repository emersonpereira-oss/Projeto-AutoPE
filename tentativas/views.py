from django.shortcuts import render
from .models import TentativaAcesso

def lista_tentativas(request):
    tentativas = TentativaAcesso.objects.all().order_by('-data_hora')
    return render(request, 'tentativas/lista.html', {'tentativas': tentativas})
