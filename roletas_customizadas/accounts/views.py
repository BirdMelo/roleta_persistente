from django.contrib.auth.hashers import check_password, make_password
from django.shortcuts import redirect, render

from accounts.forms import LoginForm, UsuarioForm
from accounts.models import Usuario

def register(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)

        if form.is_valid():
            usuario = form.save(commit=False)
            usuario.senha = make_password(form.cleaned_data['senha'])
            usuario.save()
            return redirect('accounts:login')
    else:
        form = UsuarioForm()

    return render(request, 'accounts/cadastro.html', {'form': form})
def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            nome = form.cleaned_data['nome']
            senha = form.cleaned_data['senha']
            usuario = Usuario.objects.filter(nome=nome).first()

            if usuario and check_password(senha, usuario.senha):
                request.session['usuario_id'] = usuario.pk
                # Quando a rota principal existir, substituir este render por:
                # return redirect('nome_da_rota')
                return render(
                    request,
                    'accounts/login.html',
                    {
                        'form': form,
                        'sucesso': 'Login realizado com sucesso.'
                    }
                )

            form.add_error(None, 'Nome ou senha inválidos.')
    else:
        form = LoginForm()

    return render(request, 'accounts/login.html', {'form': form})