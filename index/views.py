from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Land
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView


class Landing(CreateView):
    model = Land
    fields = ['nome_empresa', 'nome_contato',
              'celular', 'email', 'interesse']
    success_url = reverse_lazy('index')


class IndexPageView(TemplateView):
    template_name = "index.html"
