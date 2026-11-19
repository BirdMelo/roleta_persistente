from django import forms
from .models import Roleta, ItemRoleta
from django.core.validators import MinLengthValidator
from django.forms import inlineformset_factory

class RoletaForm(forms.ModelForm):
    nome = forms.CharField(
        label='*Nome',
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'Digite o nome da roleta',
            'class': 'inputs',
            'id': 'roleta_name'
        })
    )
    descricao = forms.CharField(
        label='Descrição',
        required=False,
        widget=forms.Textarea(attrs={
            'rows': 4,
            'placeholder':'Digite uma descrição para a roleta',
            'class': 'inputs',
            'id': 'roleta_description'
        })
    )
    texto_botao_giro = forms.CharField(
        label='Texto do botão',
        max_length=45,
        required=False,
        widget=forms.TextInput(attrs={
            'placeholder': 'Girar!',
            'class': 'inputs',
            'id': 'roleta_text_button'
        })
    )
    cor_bg = forms.CharField(
        label='Cor de fundo',
        max_length=7,
        validators=[MinLengthValidator(7)],
        required=False,
        widget=forms.TextInput(attrs={
            'type': 'color',
            'class': 'select_color',
            'id': 'roleta_select_color',
        }),
        initial= '#6C3CE9'
    )
    remover_fatia_sorteada = forms.BooleanField(
        label='Remover fatia sorteada',
        required=False,
        widget=forms.CheckboxInput(attrs={
            'class': 'toggle',
            'id': 'roleta_is_removable_slice'
        })
    )

    class Meta:
        model = Roleta
        fields = [
            'nome',
            'descricao',
            'texto_botao_giro',
            'cor_bg',
            'remover_fatia_sorteada'
        ]

class ItemRoletaForm(forms.ModelForm):
    texto = forms.CharField(
        label='*Item',
        max_length=45,
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'Texto para aparecer na roleta',
            'class': 'inputs',
            'id': 'item_texto'
        })
    )
    cor_bg = forms.CharField(
        label='cor de fundo',
        max_length=7,
        validators=[MinLengthValidator(7)],
        required=False,
        widget=forms.TextInput(attrs={
            'type': 'color',
            'class': 'select_color',
            'id': 'item_select_color'
        })
    )
    peso = forms.FloatField(
        label='Peso',
        required=False,
        initial=1,
        min_value=1,
        max_value=10,
        widget=forms.NumberInput(attrs={
            'class': 'inputs',
            'id': 'item_peso',
            'type': 'number',
            'min': '1',
            'max': '10',
            'step': '0.1',
            'placeholder': 'Ex: 1.5'
        })
    )

    def clean_peso(self):
        peso = self.cleaned_data.get('peso')
        return peso if peso is not None else 1

    class Meta:
        model = ItemRoleta
        fields = ['texto', 'cor_bg', 'peso']

ItemRoletaFormSet = inlineformset_factory(
    Roleta,
    ItemRoleta,
    form=ItemRoletaForm,
    extra=0,
    min_num=2,
    validate_min=True,
    can_delete=False
)
