from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Cliente

def index(request):
    return render(request, 'clientes/index.html')

def cadastro_cliente(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        cpf = request.POST.get('cpf')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')
        data_nascimento = request.POST.get('data_nascimento')
        senha = request.POST.get('senha')
        foto = request.FILES.get('foto')

        if Cliente.objects.filter(email=email).exists():
            messages.error(request, "Email já cadastrado.")
            return redirect('clientes:cadastro')

        cliente = Cliente(
            nome=nome, cpf=cpf, email=email,
            telefone=telefone, data_nascimento=data_nascimento,
            foto_faceid=foto
        )
        cliente.set_password(senha)
        cliente.save()
        messages.success(request, "Cadastro realizado!")
        return redirect('clientes:login')

    return render(request, 'clientes/cadastro.html')

def login_cliente(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        try:
            cliente = Cliente.objects.get(email=email)
            if cliente.check_password(senha):
                request.session['cliente_id'] = cliente.id
                return redirect('dashboard')
            else:
                messages.error(request, "Senha incorreta.")
        except Cliente.DoesNotExist:
            messages.error(request, "Email não encontrado.")
    return render(request, 'clientes/login.html')

def perfil_cliente(request):
    cliente_id = request.session.get('cliente_id')
    if not cliente_id:
        return redirect('clientes:login')
    cliente = get_object_or_404(Cliente, id=cliente_id)
    return render(request, 'clientes/perfil.html', {'cliente': cliente})

def logout_cliente(request):
    request.session.flush()
    return redirect('clientes:login')
