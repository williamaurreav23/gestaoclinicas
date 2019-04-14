from django.urls import path

from . import views

urlpatterns = [
    path('', views.grh, name='grh'),
    path('desempenho.html', views.desempenho, name='desempenho'),
]