from django.urls import path

from . import views


app_name = 'roletas'
urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('cadastro/', views.register, name='cadastro'),
    # path('roleta/', views.roleta, name='roleta'),
    # path('alterar/', views.alterar, name='alterar')
]