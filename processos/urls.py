from django.urls import path
from . import views
from .views import AtivoCreate, PassivoCreate
from .views import AtivosView, RentView, RentabilidadeDetail
from dashboard.dash_apps import DjangoDash

urlpatterns = [

    path('ativo/', AtivoCreate.as_view(), name='ativo'),
    path('<int:pk>/', AtivosView.as_view(), name='ativos'),
    path('passivo/', PassivoCreate.as_view(), name='passivo'),
    path('rentabilidade/', RentView.as_view(), name='rentabilidade'),
    path('rentabilidade/<int:pk>/',
         RentabilidadeDetail.as_view(), name='investimento'),
]
