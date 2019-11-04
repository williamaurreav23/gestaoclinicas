from rest_framework import serializers
from dashboard.models import bdclientes


class ClientesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = bdclientes
        fields = ['id', 'nome', 'sobrenome', 'cnpj', 'celular', 'email', 'foto']
