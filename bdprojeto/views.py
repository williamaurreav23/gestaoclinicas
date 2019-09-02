from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from .models import bdclientes
from django.utils import timezone
from django.urls import reverse_lazy

class listcliente(ListView):
    model = bdclientes

class ClienteDetail(DetailView):
    model = bdclientes

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

class ClienteCreate(CreateView):
    model = bdclientes
    fields = ['id_cliente','nome', 'sobrenome', 'cnpj', 'celular', 'email' ]
    success_url = reverse_lazy('list')

class ClienteUpdate(UpdateView):
    model = bdclientes
    fields = ['nome', 'sobrenome', 'cnpj', 'celular', 'email' ]
    success_url = reverse_lazy('list')

class ClienteDelete(DeleteView):
    model = bdclientes
    success_url = reverse_lazy('list')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context
