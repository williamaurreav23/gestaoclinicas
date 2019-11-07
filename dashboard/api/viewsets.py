from rest_framework import viewsets
from dashboard.api.serializers import ClientesSerializer
from dashboard.models import Clientes


class ClientesViewset(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    serializer_class = ClientesSerializer

    def get_queryset(self):
        return Clientes.objects.filter()