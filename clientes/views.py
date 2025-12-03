from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Cliente

# -----------------------------
# CADASTRO DO CLIENTE
# -----------------------------
def cadastro_cliente(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        cpf = request.POST.get('cpf')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')
        data_nascimento = request.POST.get('data_nascimento')
        senha = request.POST.get('senha')
        foto = request.FILES.get('foto')

        # criar cliente
        cliente = Cliente.objects.create(
            nome=nome,
            cpf=cpf,
            email=email,
            telefone=telefone,
            data_nascimento=data_nascimento,
            senha_temporaria=senha,
            foto_faceid=foto
        )

        messages.success(request, "Cadastro realizado com sucesso!")
        return redirect('login_cliente')

    return render(request, 'clientes/cadastro.html')


# -----------------------------
# LOGIN DO CLIENTE
# -----------------------------
def login_cliente(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        try:
            cliente = Cliente.objects.get(email=email, senha_temporaria=senha)
            request.session['cliente_id'] = cliente.id
            return redirect('perfil_cliente')
        except Cliente.DoesNotExist:
            messages.error(request, "Email ou senha inválidos.")

    return render(request, 'clientes/login.html')


# -----------------------------
# PERFIL DO CLIENTE
# -----------------------------
def perfil_cliente(request):
    if 'cliente_id' not in request.session:
        return redirect('login_cliente')

    cliente = get_object_or_404(Cliente, id=request.session['cliente_id'])
    return render(request, 'clientes/perfil.html', {'cliente': cliente})
