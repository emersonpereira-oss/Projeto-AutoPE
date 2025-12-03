from django.shortcuts import render
from .models import TentativaAcesso 

def lista_tentativas(request):
    tentativas = TentativaAcesso.objects.all()
    return render(request, 'tentativas/lista.html', {'tentativas': tentativas})

def registrar_tentativa(request):
    if request.method == 'POST':
        TentativaAcesso.objects.create(
            ip=request.POST.get('ip'),
            sucesso=request.POST.get('sucesso') == '1'
        )
        return render(request, 'tentativas/ok.html')

    return render(request, 'tentativas/registrar.html')
