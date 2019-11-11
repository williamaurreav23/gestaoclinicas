from rest_framework import viewsets
from dashboard.api.serializers import ClientesSerializer, FuncionarioSerializer, AtivosSerializer, PassivosSerializer
from dashboard.models import Clientes, Funcionario, Ativos, Passivos


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

class AtivosViewset(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    serializer_class = AtivosSerializer

    def get_queryset(self):
        return Ativos.objects.filter()

class PassivosViewset(viewsets.ModelViewSet):
        """
        API endpoint that allows users to be viewed or edited.
        """
        serializer_class = PassivosSerializer

        def get_queryset(self):
            return Passivos.objects.filter()