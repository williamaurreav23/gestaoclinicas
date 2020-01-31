from rest_framework import viewsets
from processos.api.serializers import AtivosSerializer, PassivosSerializer
from processos.models import Ativos, Passivos


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
