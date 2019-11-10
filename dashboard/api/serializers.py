from rest_framework import serializers
from dashboard.models import Clientes, Funcionario


class ClientesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Clientes
        fields = ['id', 'nome', 'sobrenome', 'cnpj', 'celular', 'email', 'foto']

class FuncionarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Funcionario
        fields = ['id_func', 'nome', 'nacionalidade', 'naturalidade_cid',
    'naturalidade_estado', 'data_nasc', 'sexo', 'estado_civil', 'mae',
    'pai', 'cor_raca', 'dependentes']