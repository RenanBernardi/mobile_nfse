# urls.py do seu aplicativo
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='index'),  # Redireciona a raiz para a tela de login
    path('login/', views.login_view, name='login'),
    path('emissao_nfse/', views.emissao_nfse, name='emissao_nfse'),
    path('endereco_servidor/', views.endereco_servidor, name='endereco_nfse'),
]

