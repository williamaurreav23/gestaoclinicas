from rest_framework import viewsets
from dashboard.api.serializers import ClientesSerializer, FuncionarioSerializer
from dashboard.models import Clientes, Funcionario


class ClientesViewset(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    serializer_class = ClientesSerializer

    def get_queryset(self):
        return Clientes.objects.filter()

class FuncionarioViewset(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    serializer_class = FuncionarioSerializer

    def get_queryset(self):
        return Funcionario.objects.filter()