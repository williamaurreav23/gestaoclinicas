from rest_framework import serializers
from dashboard.models import Clientes, Funcionario, Ativos, Passivos


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


class AtivosSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ativos
        fields = ['id_ativo', 'tipo_ativo', 'descricao_ativo', 'valor_ativo', 'data_ativo']

class PassivosSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Passivos
        fields = ['id_passivo', 'tipo_passivo', 'descricao_passivo', 'valor_passivo', 'data_passivo']