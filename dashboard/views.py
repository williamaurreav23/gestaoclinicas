import dash
from django_plotly_dash import DjangoDash
import dash_html_components as html
import dash_core_components as dcc
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from dashboard.models import Clientes, Gestor, Funcionario
from django.views.generic.base import TemplateView


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


# Create your views here.


app = DjangoDash('SimpleExample')   # replaces dash.Dash

app.layout = html.Div([
    dcc.RadioItems(
        id='dropdown-color',
        options=[{'label': c, 'value': c.lower()}
                 for c in ['Red', 'Green', 'Blue']],
        value='red'
    ),
    html.Div(id='output-color'),
    dcc.RadioItems(
        id='dropdown-size',
        options=[{'label': i,
                  'value': j} for i, j in [('L', 'large'), ('M', 'medium'), ('S', 'small')]],
        value='medium'
    ),
    html.Div(id='output-size')

])


@app.callback(
    dash.dependencies.Output('output-color', 'children'),
    [dash.dependencies.Input('dropdown-color', 'value')])
def callback_color(dropdown_value):
    return "The selected color is %s." % dropdown_value


@app.callback(
    dash.dependencies.Output('output-size', 'children'),
    [dash.dependencies.Input('dropdown-color', 'value'),
     dash.dependencies.Input('dropdown-size', 'value')])
def callback_size(dropdown_color, dropdown_size):
    return "The chosen T-shirt is a %s %s one." % (dropdown_size,
                                                   dropdown_color)


def graf(requests):
    return render(requests, 'dashboard.html')
