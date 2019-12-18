from rest_framework import serializers
from dashboard.models import Clientes


class ClientesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Clientes
        fields = ['id', 'nome', 'sobrenome', 'cnpj', 'celular', 'email', 'foto']
