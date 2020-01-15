from django.urls import path
from . import views
from .views import ClienteDetail, ClienteCreate, ListClientes, ClienteUpdate, ClienteDelete
from .views import GestorCreate, FuncionarioCreate
from .views import AtivoCreate, PassivoCreate
from .views import AtivosView
# from dashboard.dash_apps import example

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('listclientes', ListClientes.as_view(), name='list'),
    path('cliente/<int:pk>/', ClienteDetail.as_view(), name='detail'),
    path('cadastro/', ClienteCreate.as_view(), name='new'),
    path('editar/<int:pk>/', ClienteUpdate.as_view(), name='update'),
    path('excluir/<int:pk>/', ClienteDelete.as_view(), name='delete'),
    path('gestor/', GestorCreate.as_view(), name='gestor'),
    path('funcionario/', FuncionarioCreate.as_view(), name='funcionario'),
    path('ativo/', AtivoCreate.as_view(), name='ativo'),
    path('<int:pk>/', AtivosView.as_view(), name='ativos'),
    path('passivo/', PassivoCreate.as_view(), name='passivo'),

]
