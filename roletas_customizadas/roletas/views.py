# view da application roletas, aqui são criadas as
# funções que chamam os templates em roletas/templates/roletas.
# Foi criado um arquivo mock_data.py para simular o dados das roletas
# para facilitar o desenvolvimento dos templates. Para sincronizar
# com o models.py é só subistituir os importes e trocar
# onde está escrito roletas por Roleta.objects.all()

from django.shortcuts import render, get_object_or_404