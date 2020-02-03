from django.urls import path
from index.views import Landing, IndexPageView
from django.views.generic.base import TemplateView

urlpatterns = [
    path('', IndexPageView.as_view(), name='index'),
    path('land_form.html', Landing.as_view(), name='land'),
    path('descricao.html', TemplateView.as_view(
        template_name='descricao.html'), name='descricao'),
    path('empresa.html', TemplateView.as_view(
        template_name='empresa.html'), name='empresa'),
    path('servicos.html', TemplateView.as_view(
        template_name='servicos.html'), name='servicos'),
    path('clientes.html', TemplateView.as_view(
        template_name='clientes.html'), name='clientes'),
    path('blog.html', TemplateView.as_view(
        template_name='blog.html'), name='blog'),
]
