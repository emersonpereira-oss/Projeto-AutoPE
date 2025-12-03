from django.shortcuts import render, get_object_or_404
from .models import Veiculo

def lista_veiculos(request):
    veiculos = Veiculo.objects.all()
    return render(request, 'veiculos/lista.html', {'veiculos': veiculos})

def detalhe_veiculo(request, id):
    veiculo = get_object_or_404(Veiculo, id=id)
    return render(request, 'veiculos/detalhe.html', {'veiculo': veiculo})
