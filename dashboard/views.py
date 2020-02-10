from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from dashboard.models import Clientes, Gestor, Funcionario
from django.views.generic.base import TemplateView
# Create your views here.
from django.shortcuts import render
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from dashboard.as_dash import dispatcher


# Login
@login_required
class DashPage(TemplateView):
    template_name = "dashboard.html"


# Listar Dados

class ListClientes(ListView):
    model = Clientes
    template_name = "clientes_list.html"


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
    success_url = reverse_lazy('index')


class FuncionarioCreate(CreateView):
    model = Funcionario
    fields = ['id_func', 'nome', 'nacionalidade', 'naturalidade_cid',
              'naturalidade_estado', 'data_nasc', 'sexo', 'estado_civil', 'mae',
              'pai', 'cor_raca', 'dependentes']


#    success_url = reverse_lazy('funcionario')
# return render(request, 'fucionario.html')


class ClienteUpdate(UpdateView):
    model = Clientes
    fields = ['nome', 'sobrenome', 'cnpj', 'celular', 'email']


#    success_url = reverse_lazy("list")


class ClienteDelete(DeleteView):
    model = Clientes

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class GestorCreate(CreateView):
    model = Gestor
    fields = ['gestor_id', 'nome', 'email', 'celular', 'especialidade']


# Gráficos
##### dash #####


def dash(request, **kwargs):
    ''' '''
    return HttpResponse(dispatcher(request))


@csrf_exempt
def dash_ajax(request):
    ''' '''
    return HttpResponse(dispatcher(request), content_type='application/json')