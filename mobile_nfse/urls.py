# urls.py do seu aplicativo
from django.urls import path
from . import views
from .views import login_view
from .views import index_view
from .views import emissao_nfse
from .views import endereco_servidor

urlpatterns = [
    path('', index_view, name='index'),  # Redireciona a raiz para a tela de login
    path('login/', login_view, name='login'),
    path('emissao_nfse/', emissao_nfse, name='emissao_nfse'),
    path('endereco_servidor/', endereco_servidor, name='endereco_servidor'),
]