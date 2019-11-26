from django.db import models

class Clientes(models.Model):

    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=30, blank=True, null=True)
    sobrenome = models.CharField(max_length=30, blank=True, null=True)
    cnpj = models.CharField(max_length=11, blank=False, null=True)
    celular = models.CharField(max_length=9, blank=True, null=True)
    email = models.CharField(max_length=254, blank=True, null=True)
    foto = models.ImageField(upload_to='fotos', null=True, blank=True)

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ["nome"]

# Create your models here.
class Gestor(models.Model):
    gestor_id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    email = models.CharField(max_length=20, blank=True, null=True)
    celular = models.CharField(max_length=11, blank=True, null=True)
    especialidade = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.nome

class Funcionario(models.Model):
    id_func = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nacionalidade = models.CharField(max_length=50, blank=True, null=True)
    naturalidade_cid = models.CharField(max_length=20, blank=True, null=True)
    naturalidade_estado = models.CharField(max_length=20, blank=True, null=True)
    data_nasc = models.DateField(blank=True, null=True)
    sexo = models.CharField(max_length=10, blank=True, null=True)
    estado_civil = models.CharField(max_length=10, blank=True, null=True)
    mae = models.CharField(max_length=50, blank=True, null=True)
    pai = models.CharField(max_length=50, blank=True, null=True)
    cor_raca = models.CharField(max_length=10, blank=True, null=True)
    dependentes = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.nome

class Clinica(models.Model):
    clinica_id = models.AutoField(primary_key=True)
    nomefantasia = models.CharField(max_length=100)
    cnpj = models.CharField(unique=True, max_length=100)
    email = models.CharField(max_length=20, blank=True, null=True)
    contato = models.CharField(max_length=11, blank=True, null=True)
    especialidade = models.CharField(max_length=30, blank=True, null=True)

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

class Contatos(models.Model):
    nome = models.CharField(max_length=50, blank=True, null=True)
    sobrenome = models.CharField(max_length=50, blank=True, null=True)
    telefone = models.CharField(max_length=9, blank=True, null=True)
    celular = models.CharField(max_length=10, blank=True, null=True)

class Empresas(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    nome_fantasia = models.CharField(db_column='nome fantasia', max_length=50, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    nome_juridico = models.CharField(db_column='nome juridico', max_length=50, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    cnpj = models.CharField(max_length=11)

class IndicadoresNegativos(models.Model):
    id = models.AutoField(primary_key=True, blank=True, null=False)
    questao = models.TextField(blank=True, null=True)

class Lucratividade(models.Model):
    id = models.AutoField(primary_key=True)
    lucro_liquido_anual = models.TextField(blank=True, null=True)
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

class Turnover(models.Model):
    id = models.AutoField(primary_key=True, blank=True, null=False)
    contratados = models.TextField(blank=True, null=True)
    desligamentos = models.TextField(blank=True, null=True)
