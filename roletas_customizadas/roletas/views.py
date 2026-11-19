# view da application roletas, aqui são criadas as
# funções que chamam os templates em roletas/templates/roletas.
# Foi criado um arquivo mock_data.py para simular o dados das roletas
# para facilitar o desenvolvimento dos templates. Para sincronizar
# com o models.py é só subistituir os importes e trocar
# onde está escrito roletas por Roleta.objects.all()

from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from roletas.forms import RoletaForm, ItemRoletaForm, ItemRoletaFormSet
from django.db import transaction

@login_required(login_url='accounts:login')
def dashboard(request):
    roletas = request.user.roletas.all()
    return render(request, 'roletas/dashboard.html', {'roletas': roletas})
@login_required(login_url='accounts:login')
def register(request):
    if request.method == 'POST':
        roleta_form = RoletaForm(request.POST)
        item_formset = ItemRoletaFormSet(request.POST)

        if roleta_form.is_valid() and item_formset.is_valid():
            with transaction.atomic():
                roleta = roleta_form.save(commit=False)
                roleta.usuario = request.user
                roleta.save()

                itens = item_formset.save(commit=False)

                for ordem, item in enumerate(itens, start=1):
                    item.roleta = roleta
                    item.ordem = ordem
                    item.save()
            return redirect('roletas:dashboard')
    else:
        roleta_form = RoletaForm()
        item_formset = ItemRoletaFormSet()

    return render(
        request,
        'roletas/cadastro.html',
        {
            'roleta_form': roleta_form,
            'item_formset': item_formset
        }
    )