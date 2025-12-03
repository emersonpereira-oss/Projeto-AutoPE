from django.shortcuts import render, redirect, get_object_or_404
from .models import Locacao
from veiculos.models import Veiculo
from clientes.models import Cliente

def lista_locacoes(request):
    locacoes = Locacao.objects.all()
    return render(request, 'locacao/lista.html', {'locacoes': locacoes})


def nova_locacao(request):
    if request.method == 'POST':
        cliente_id = request.POST.get('cliente_id')
        veiculo_id = request.POST.get('veiculo_id')
        dias = request.POST.get('dias')

        cliente = Cliente.objects.get(id=cliente_id)
        veiculo = Veiculo.objects.get(id=veiculo_id)

        Locacao.objects.create(
            cliente=cliente,
            veiculo=veiculo,
            dias=dias
        )

        return redirect('locacao:lista')

    return render(request, 'locacao/nova.html')


def detalhe_locacao(request, id):
    locacao = get_object_or_404(Locacao, id=id)
    return render(request, 'locacao/detalhe.html', {'locacao': locacao})
