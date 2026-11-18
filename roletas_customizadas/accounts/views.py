from django.contrib.auth import authenticate, login as auth_login, logout
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from accounts.forms import LoginForm, UsuarioForm
from .models import Usuario
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('accounts:login')
    else:
        form = UsuarioForm()

    return render(request, 'accounts/cadastro.html', {'form': form})
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            usuario = authenticate(
                request,
                username=username,
                password=password
            )

            if usuario is not None:
                auth_login(request, usuario)
                return redirect('roletas:dashboard') #substituir accounst:login para roletas:dashboard

            form.add_error(None, 'Usuário ou senha inválidos.')
    else:
        form = LoginForm()

    return render(request, 'accounts/login.html', {'form': form})

@login_required(login_url='accounts:login')
def perfil_view(request):
    return render(request, 'accounts/perfil.html')

@login_required(login_url='accounts:login')
def alterar_usuario(request):
    usuario = request.user
    
    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=usuario)
        
        if form.is_valid():
            form.save()
            messages.success(request, 'Alteração de conta feita.')
            return redirect('accounts:perfil')
        
        messages.error(request, 'Erro no preenchimento do formulário.')
        return render(request, 'accounts/alterar.html', {'form': form})
    
    form = UsuarioForm(instance=usuario)
    return render(request, 'accounts/alterar.html', {'form': form})

@login_required(login_url='accounts:login')
def excluir_usuario(request):
    usuario = request.user
    
    if request.method == 'POST':
        logout(request)
        usuario.delete()
        messages.success(request, 'Usuário deletado com sucesso')
        return redirect('accounts:login')
    return render(request, 'accounts/perfil.html', {'user': usuario})