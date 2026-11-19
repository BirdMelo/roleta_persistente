from django.urls import path

from . import views

app_name = 'accounts'

urlpatterns = [
    path('cadastro/', views.register, name='cadastro'),
    path('login/', views.login_view, name='login'),
    path('perfil/', views.perfil_view, name='perfil'),
    path('tema/', views.atualizar_tema, name='tema'),
    path('alterar/', views.alterar_usuario, name='alterar'),
    path('excluir/', views.excluir_usuario, name='excluir'),
]