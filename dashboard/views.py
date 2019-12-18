from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.views.generic.edit import FormView
from .models import Clientes, Gestor
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


# Formulários

class listcliente(ListView):
    model = Clientes

class ClienteDetail(DetailView):
    model = Clientes

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

class ClienteCreate(CreateView):
    model = Clientes
    fields = ['nome', 'sobrenome', 'cnpj', 'celular', 'email' ]
    success_url = reverse_lazy('list')

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

output_file("dashboard/templates/bar_stacked.html")

indices = ['despesas', 'receitas', 'lucro']
years = ["2017", "2018", "2019"]
colors = ["#c9d9d3", "#718dbf", "#e84d60"]

data = {'indices' : indices,
        '2017'   : [23, 14, 47],
        '2018'   : [53, 36, 43],
        '2019'   : [38, 27, 44]}

p = figure(x_range=indices, plot_height=250, title="indices da Empresa",
           toolbar_location=None, tools="hover", tooltips="$name @indices: @$name")

p.vbar_stack(years, x='indices', width=0.9, color=colors, source=data,
             legend=[value(x) for x in years])

p.y_range.start = 0
p.x_range.range_padding = 0.1
p.xgrid.grid_line_color = None
p.axis.minor_tick_line_color = None
p.outline_line_color = None
p.legend.location = "top_left"
p.legend.orientation = "horizontal"

from bokeh.plotting import figure, show, output_file
from bokeh.sampledata.iris import flowers

colormap = {'setosa': 'red', 'versicolor': 'green', 'virginica': 'blue'}
colors = [colormap[x] for x in flowers['species']]

p = figure(title = "Iris Morphology")
p.xaxis.axis_label = 'Petal Length'
p.yaxis.axis_label = 'Petal Width'

p.circle(flowers["petal_length"], flowers["petal_width"],
         color=colors, fill_alpha=0.2, size=10)

output_file("dashboard/templates/iris.html", title="iris.py example")


#DESEMPENHO


# Create your views here.

def rotatividade(admissoes, demissoes, colaboadores):
    numerador = (admissoes + demissoes) / 2
    racio = numerador / colaboadores
    taxa = racio * 100
    print("o valor de rotatividade foi de :", taxa, "%")


def grh(request):
    return render(request, 'funcionarios.html')

def desempenho(request):
    return render(request, 'desempenho.html')