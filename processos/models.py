from django.db import models

# Create your models here.


class Ativos(models.Model):
    id_ativo = models.AutoField(primary_key=True)
    tipo_ativo = models.CharField(max_length=20, blank=True, null=True)
    descricao_ativo = models.CharField(max_length=20, blank=True, null=True)
    valor_ativo = models.IntegerField(blank=True, null=True)
    data_ativo = models.DateField(blank=True, null=True)


class Passivos(models.Model):
    id_passivo = models.AutoField(primary_key=True)
    tipo_passivo = models.CharField(max_length=20, blank=True, null=True)
    descricao_passivo = models.CharField(max_length=20, blank=True, null=True)
    valor_passivo = models.IntegerField(blank=True, null=True)
    data_passivo = models.DateField(blank=True, null=True)


class IndicadoresNegativos(models.Model):
    id = models.AutoField(primary_key=True, blank=True, null=False)
    questao = models.TextField(blank=True, null=True)


class Lucratividade(models.Model):
    id = models.AutoField(primary_key=True)
    lucro_liquido_anual = models.TextField(blank=True, null=True)
    receita_total_anual = models.TextField(blank=True, null=True)


class Receita(models.Model):
    id = models.AutoField(primary_key=True)
    receita_total = models.TextField(blank=True, null=True)
    receita_total_anual = models.TextField(blank=True, null=True)


class Despesa(models.Model):
    id = models.AutoField(primary_key=True)
    receita_total = models.TextField(blank=True, null=True)
    receita_total_anual = models.TextField(blank=True, null=True)


class Roi(models.Model):
    id = models.AutoField(primary_key=True, blank=True, null=False)
    receita = models.TextField(blank=True, null=True)
    custo = models.TextField(blank=True, null=True)
    item = models.TextField(blank=True, null=True)


class TaxaConversao(models.Model):
    visitantes = models.AutoField(primary_key=True, blank=True, null=False)
    id = models.TextField(blank=True, null=True)
    conversoes = models.TextField(blank=True, null=True)


class TicketMedioVendas(models.Model):
    id = models.AutoField(primary_key=True, blank=True, null=False)
    total_receita = models.TextField(blank=True, null=True)
    total_vendas = models.TextField(blank=True, null=True)
    nr_compras = models.TextField(blank=True, null=True)
    periodo = models.DateField(blank=True, null=True)


class Rentabilidade(models.Model):
    id = models.AutoField(primary_key=True, blank=True, null=False)
    data_inicio = models.DateField(blank=True, null=True)
    data_fim = models.DateField(blank=True, null=True)
    investimento = models.DecimalField(
        max_digits=1000, decimal_places=2, null=True)
    lucro_liquido = models.DecimalField(
        max_digits=1000, decimal_places=2, null=True)
    rentabilidade = models.DecimalField(
        max_digits=1000, decimal_places=2, null=True)
