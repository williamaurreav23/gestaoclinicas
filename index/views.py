from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.views.generic.edit import FormView
from .models import registerclientes
from index.forms import ClienteForms
from django.utils import timezone
from django.urls import reverse_lazy

class listcliente(ListView):
    model = registerclientes

class ClienteDetail(DetailView):
    model = registerclientes

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

class registerclient(CreateView):
    model = registerclientes
    fields = ['nome', 'sobrenome', 'cnpj', 'celular', 'email' ]
    success_url = reverse_lazy('listclientes')

class ClienteUpdate(UpdateView):
    model = registerclientes
    fields = ['nome', 'sobrenome', 'cnpj', 'celular', 'email' ]
    success_url = reverse_lazy('list')

class ClienteDelete(DeleteView):
    model = registerclientes
    success_url = reverse_lazy('list')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context











# def registerclient(request):
#     if request.method =='POST' :
#         form = ClienteForms(request.POST)

#         if form.is_valid():
#             redirect('index')
#         else:
#             form = ClienteForms()
#         context = {'form' : form}

#         return render(request, 'index.html', context)



def index(request):
    return render(request, 'index.html')


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
