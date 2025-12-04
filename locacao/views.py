from django.shortcuts import render, redirect, get_object_or_404
from .models import Locacao
from clientes.models import Cliente
from veiculos.models import Veiculo

def lista_locacoes(request):
    locacoes = Locacao.objects.all()
    return render(request, 'locacao/lista.html', {'locacoes': locacoes})

def nova_locacao(request):
    if request.method == 'POST':
        cliente_id = request.POST.get('cliente_id')
        veiculo_id = request.POST.get('veiculo_id')
        data_prevista = request.POST.get('data_prevista')
        cliente = get_object_or_404(Cliente, id=cliente_id)
        veiculo = get_object_or_404(Veiculo, id=veiculo_id)
        loc = Locacao.objects.create(cliente=cliente, veiculo=veiculo, data_prevista=data_prevista)
        return redirect('locacao:lista')
    veiculos = Veiculo.objects.filter(status='disponivel')
    return render(request, 'locacao/nova.html', {'veiculos': veiculos})

def detalhe_locacao(request, id):
    loc = get_object_or_404(Locacao, id=id)
    return render(request, 'locacao/detalhe.html', {'locacao': loc})
