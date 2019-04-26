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
]