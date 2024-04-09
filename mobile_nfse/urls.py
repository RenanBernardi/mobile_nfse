# urls.py do seu aplicativo
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='index'),  # Redireciona a raiz para a tela de login
    path('login/', views.login_view, name='login'),
    path('emitir_nfse/', views.emitir_nfse, name='emitir_nfse'),
]

