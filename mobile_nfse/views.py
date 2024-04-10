from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login


def index_view(request):
    return render(request, 'index.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('emissao_nfse')  # Redireciona para a tela de emissão
        else:
            return render(request, 'login.html', {'error': 'Credenciais inválidas'})
    else:
        return render(request, 'login.html')  # Retorna a página de login para o método GET


def emissao_nfse(request):
    if request.user.is_authenticated:
        # Aqui você pode colocar a lógica para a emissão de NFSe
        nfse_gerada = {
            'numero': 123,
            'valor': 100.00,
            'codigo_verificacao': 'ABC123XYZ'
        }
        return JsonResponse(nfse_gerada)
    else:
        return redirect('emissao_nfse.html')  # Redireciona para a tela de login se o usuário não estiver autenticado
