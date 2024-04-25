from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login


def index_view(request):
    return render(request, 'index.html')

def login_view(request):
    if request.method == 'POST':
            return redirect('emissao_nfse')
    else:
            return render(request, 'login.html')


def emissao_nfse(request):
    if request.method == 'POST':
        return redirect('emissao_nfse')
    else:
        return render(request, 'emissao_nfse.html')


def endereco_servidor(request):
     if request.method == 'POST':
          return redirect('endereco_servidor')
     else:
          return render(request, 'endereco_servidor.html')