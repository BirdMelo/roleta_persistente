from django.urls import path

from . import views

app_name = 'accounts'

urlpatterns = [
    path('cadastro/', views.register, name='cadastro'),
    path('login/', views.login, name='login'),
    # path('perfil/', views.perfil, name='perfil')
]