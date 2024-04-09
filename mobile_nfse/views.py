from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login



def index_view(request):
    return render(request, 'index.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('emitir_nfse')  # Redireciona para a tela de emissão
        else:
            return render(request, 'login.html', {'error': 'Credenciais inválidas'})
    else:
        return render(request, 'login.html')


def emitir_nfse(request):
    if request.method == 'POST':
        dados = request.POST
        # Lógica para emitir NFSe aqui
        nfse_gerada = {
            'numero': 123,
            'valor': 100.00,
            'codigo_verificacao': 'ABC123XYZ'
        }
        return JsonResponse(nfse_gerada)
    else:
        return JsonResponse({'error': 'Método não permitido'}, status=405)


def emitir_nfse(request):
        # Lógica para emitir NFSe
    return render(request, 'emitir_nfse.html')
