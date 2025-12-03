from django.shortcuts import render, redirect
from .models import Pagamento
from locacao.models import Locacao

def lista_pagamentos(request):
    pagamentos = Pagamento.objects.all()
    return render(request, 'pagamentos/lista.html', {'pagamentos': pagamentos})


def novo_pagamento(request):
    if request.method == 'POST':
        locacao_id = request.POST.get('locacao_id')
        valor = request.POST.get('valor')
        metodo = request.POST.get('metodo')

        locacao = Locacao.objects.get(id=locacao_id)

        Pagamento.objects.create(
            locacao=locacao,
            valor=valor,
            metodo=metodo
        )

        return redirect('pagamentos:lista')

    return render(request, 'pagamentos/novo.html')
