from rest_framework import serializers
from processos.models import Ativos, Passivos


class AtivosSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ativos
        fields = ['id_ativo', 'tipo_ativo',
                  'descricao_ativo', 'valor_ativo', 'data_ativo']


class PassivosSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Passivos
        fields = ['id_passivo', 'tipo_passivo',
                  'descricao_passivo', 'valor_passivo', 'data_passivo']
