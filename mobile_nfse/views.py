from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.template.loader import render_to_string

html_content = render_to_string('login.html')
html_content = render_to_string('index.html')
html_content = render_to_string('endereco_servidor.html')
html_content= render_to_string('emissao_nfse.html')
html_content = render_to_string('totalizacao.html')

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

def totalizacao(request):
    if request.method == 'POST':
        return redirect('totalizacao')
    else:
        valor_servico = float(request.POST.get('valor_servico', 0))
        desconto = float(request.POST.get('desconto', 0))
        tipo_desconto = request.POST.get('tipo_desconto')

        valor_desconto = None
        if tipo_desconto == 'porcentagem':
            valor_desconto = (valor_servico * desconto) / 100
        elif tipo_desconto == 'valor':
            valor_desconto = desconto

        if valor_desconto is not None:
            total = valor_servico - valor_desconto
        else:
            total = valor_servico

        return render(request, 'totalizacao.html', {'total': total})
    
    