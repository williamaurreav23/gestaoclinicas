from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Land
from django.urls import reverse_lazy


class Landing(CreateView):
    model = Land
    fields = ['nome_empresa', 'nome_contato',
              'celular', 'email', 'interesse']
    success_url = reverse_lazy('index')


def index(request):
    return render(request, 'index.html')


def land(request):
    return render(request, 'land_form.html')


def gestao(request):
    return render(request, 'gestao.html')


def top(request):
    return render(request, 'top.html')


def planejamento(request):
    return render(request, 'planejamento.html')


def marketing(request):
    return render(request, 'marketing.html')


def design(request):
    return render(request, 'design.html')


def data(request):
    return render(request, 'data.html')


def empresa(request):
    return render(request, 'empresa.html')


def equipe(request):
    return render(request, 'equipe.html')


def servicos(request):
    return render(request, 'servicos.html')


def clientes(request):
    return render(request, 'clientes.html')


def parceiros(request):
    return render(request, 'parceiros.html')


def blog(request):
    return render(request, 'blog.html')
