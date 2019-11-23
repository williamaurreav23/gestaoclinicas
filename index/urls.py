from django.urls import path
from index import views


urlpatterns = [
    path('', views.index, name='index'),
    path('gestao.html', views.gestao, name='gestao'),
    path('top.html', views.top, name='top'),
    path('planejamento.html', views.planejamento, name='planejamento'),
    path('marketing.html', views.marketing, name='marketing'),
    path('design.html', views.design, name='design'),
    path('data.html', views.data, name='data'),
    path('empresa.html', views.empresa, name='empresa'),
    path('equipe.html', views.equipe, name='equipe'),
    path('servicos.html', views.servicos, name='servicos'),
    path('parceiros.html', views.parceiros, name='parceiros'),
    path('clientes.html', views.clientes, name='clientes'),
    path('blog.html', views.blog, name='blog'),
]