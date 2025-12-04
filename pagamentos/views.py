from django.shortcuts import render, redirect, get_object_or_404
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
        loc = get_object_or_404(Locacao, id=locacao_id)
        pag = Pagamento.objects.create(valor=valor, metodo=metodo, status='pago')
        loc.pagamento = pag
        loc.save()
        return redirect('pagamentos:lista')
    locacoes = Locacao.objects.filter(pagamento__isnull=True)
    return render(request, 'pagamentos/novo.html', {'locacoes': locacoes})
