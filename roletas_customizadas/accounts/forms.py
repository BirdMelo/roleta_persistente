from django import forms
from .models import Usuario

class UsuarioForm(forms.ModelForm):
    nome = forms.CharField(
        label='*Nome',
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'Digite seu nome',
            'class': 'inputs',
            'id': 'user_name'
        })
    )
    senha = forms.CharField(
        label='*Senha',
        max_length=120,
        required=True,
        widget= forms.PasswordInput(attrs={
            'placeholder': 'Digite sua senha',
            'class': 'inputs',
            'id': 'user_password'
        })
    )
    
    class Meta:
        model = Usuario
        fields = ['nome', 'senha']


class LoginForm(forms.Form):
    nome = forms.CharField(
        label='*Nome',
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'Digite seu nome',
            'class': 'inputs',
            'id': 'login_name'
        })
    )
    senha = forms.CharField(
        label='*Senha',
        max_length=120,
        required=True,
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Digite sua senha',
            'class': 'inputs',
            'id': 'login_password'
        })
    )
        