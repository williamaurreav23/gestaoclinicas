from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from .models import Clientes, Gestor, Funcionario
from dashboard.forms import ClienteForms
from django.utils import timezone
from django.urls import reverse_lazy
from bokeh.core.properties import value
from bokeh.io import show, output_file
from bokeh.plotting import figure

#Login

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')


@login_required
def listclientes(request):
    return render(request, 'listclientes.html')


# Listar Dados

class listcliente(ListView):
    model = Clientes

class ClienteDetail(DetailView):
    model = Clientes

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context
#Criar Dados
class ClienteCreate(CreateView):
    model = Clientes
    fields = ['nome', 'sobrenome', 'cnpj', 'celular', 'email' ]
    success_url = reverse_lazy('list')

class FuncionarioCreate(CreateView):
    model = Funcionario
    fields = ['id_func', 'nome', 'nacionalidade', 'naturalidade_cid', 
    'naturalidade_estado', 'data_nasc', 'sexo', 'estado_civil', 'mae',
    'pai', 'cor_raca', 'dependentes' ]
    success_url = reverse_lazy('funcionario')

class ClienteUpdate(UpdateView):
    model = Clientes
    fields = ['nome', 'sobrenome', 'cnpj', 'celular', 'email' ]
    success_url = reverse_lazy('list')

class ClienteDelete(DeleteView):
    model = Clientes
    success_url = reverse_lazy('list')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context
    
class ClientesViewset(object):
    pass

#Gestores

class GestorCreate(CreateView):
    model = Gestor
    fields = ['gestor_id', 'nome', 'email', 'celular', 'especialidade']
    success_url = reverse_lazy('list')


# Gráficos


#DESEMPENHO


# Create your views here.

def rotatividade(admissoes, demissoes, colaboadores):
    numerador = (admissoes + demissoes) / 2
    racio = numerador / colaboadores
    taxa = racio * 100
    print("o valor de rotatividade foi de :", taxa, "%")


def desempenho(request):
    return render(request, 'desempenho.html')