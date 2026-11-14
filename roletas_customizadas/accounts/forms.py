from django import forms

from .models import Usuario

class UsuarioForm(forms.ModelForm):
    password = forms.CharField(
        label='Senha',
        widget=forms.PasswordInput(attrs={
            'class': 'inputs',
            'id': 'register_password'
        })
    )

    class Meta:
        model = Usuario
        fields = ['username', 'password']
        labels = {
            'username': 'Nome',
        }
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'inputs',
                'id': 'register_username'
            }),
        }

    def save(self, commit=True):
        usuario = super().save(commit=False)
        usuario.set_password(self.cleaned_data['password'])
        if commit:
            usuario.save()
        return usuario


class LoginForm(forms.Form):
    username = forms.CharField(
        label='Usuário',
        max_length=150,
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'Digite seu usuário',
            'class': 'inputs',
            'id': 'login_username'
        })
    )
    password = forms.CharField(
        label='Senha',
        required=True, 
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Digite sua senha',
            'class': 'inputs',
            'id': 'login_password'
        })
    )
        