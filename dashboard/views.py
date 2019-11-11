from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic.detail import DetailView
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Clientes, Gestor, Funcionario, Ativos, Passivos
from django.utils import timezone
from django.urls import reverse_lazy
from bokeh.core.properties import value
from bokeh.io import show, output_file
from bokeh.plotting import figure

from django.http import HttpResponseRedirect
from .forms import AtivosForm

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = AtivosForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/dashboard/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = AtivosForm()

    return render(request, "ativos_form.html", {'form': form})

# Login

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')


# Listar Dados

class ListClientes(ListView):
    template_name = "clientes_list.html"
    queryset = Clientes.objects.all()



class ClienteDetail(DetailView):
    model = Clientes

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


# Criar Dados
class ClienteCreate(CreateView):
    model = Clientes
    fields = ['nome', 'sobrenome', 'cnpj', 'celular', 'email', 'foto']
    success_url = reverse_lazy('list')

class FuncionarioCreate(CreateView):
    model = Funcionario
    fields = ['id_func', 'nome', 'nacionalidade', 'naturalidade_cid',
              'naturalidade_estado', 'data_nasc', 'sexo', 'estado_civil', 'mae',
              'pai', 'cor_raca', 'dependentes']
    success_url = reverse_lazy('funcionario')


class ClienteUpdate(UpdateView):
    model = Clientes
    fields = ['nome', 'sobrenome', 'cnpj', 'celular', 'email']
    success_url = reverse_lazy("list")


class ClienteDelete(DeleteView):
    model = Clientes
    success_url = reverse_lazy('list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class AtivoCreate(CreateView):
    model = Ativos
    fields = ['id_ativo', 'tipo_ativo', 'descricao_ativo', 'valor_ativo', 'data_ativo']
    success_url = reverse_lazy("dashboard")

class PassivoCreate(CreateView):
    model = Passivos
    fields = ['id_passivo', 'tipo_passivo', 'descricao_passivo', 'valor_passivo', 'data_passivo']
    success_url = reverse_lazy("dashboard")

# Gestores

class GestorCreate(CreateView):
    model = Gestor
    fields = ['gestor_id', 'nome', 'email', 'celular', 'especialidade']
    success_url = reverse_lazy('list')


# Gráficos


# DESEMPENHO


# Create your views here.

def rotatividade(admissoes, demissoes, colaboadores):
    numerador = (admissoes + demissoes) / 2
    racio = numerador / colaboadores
    taxa = racio * 100
    print("o valor de rotatividade foi de :", taxa, "%")


def desempenho(request):
    return render(request, 'desempenho.html')
