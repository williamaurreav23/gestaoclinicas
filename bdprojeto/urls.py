from django.urls import path
from .views import ClienteDetail, ClienteCreate, listcliente, ClienteUpdate, ClienteDelete

urlpatterns = [
    path('listcliente/', listcliente.as_view(), name='list'),
    path('cliente/<int:pk>/', ClienteDetail.as_view(), name='detail'),
    path('cadastro/', ClienteCreate.as_view() , name='new'),
    path('editar/<int:pk>/', ClienteUpdate.as_view(), name='update'),
    path('excluir/<int:pk>/', ClienteDelete.as_view(), name='delete'),

]
