from django.db import models


class Clientes(models.Model):

    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=30, blank=True, null=True)
    sobrenome = models.CharField(max_length=30, blank=True, null=True)
    cnpj = models.CharField(max_length=11, blank=False, null=True)
    celular = models.CharField(max_length=9, blank=True, null=True)
    email = models.CharField(max_length=254, blank=True, null=True)
    foto = models.ImageField(upload_to='fotos', null=True, blank=True)

    class Meta:
        ordering = ["nome"]

# Create your models here.


class Gestor(models.Model):
    gestor_id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    email = models.CharField(max_length=20, blank=True, null=True)
    celular = models.CharField(max_length=11, blank=True, null=True)
    especialidade = models.CharField(max_length=30, blank=True, null=True)


class Funcionario(models.Model):
    id_func = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nacionalidade = models.CharField(max_length=50, blank=True, null=True)
    naturalidade_cid = models.CharField(max_length=20, blank=True, null=True)
    naturalidade_estado = models.CharField(
        max_length=20, blank=True, null=True)
    data_nasc = models.DateField(blank=True, null=True)
    sexo = models.CharField(max_length=10, blank=True, null=True)
    estado_civil = models.CharField(max_length=10, blank=True, null=True)
    mae = models.CharField(max_length=50, blank=True, null=True)
    pai = models.CharField(max_length=50, blank=True, null=True)
    cor_raca = models.CharField(max_length=10, blank=True, null=True)
    dependentes = models.IntegerField(blank=True, null=True)


class Clinica(models.Model):
    clinica_id = models.AutoField(primary_key=True)
    nomefantasia = models.CharField(max_length=100)
    cnpj = models.CharField(unique=True, max_length=100)
    email = models.CharField(max_length=20, blank=True, null=True)
    contato = models.CharField(max_length=11, blank=True, null=True)
    especialidade = models.CharField(max_length=30, blank=True, null=True)


class Contatos(models.Model):
    nome = models.CharField(max_length=50, blank=True, null=True)
    sobrenome = models.CharField(max_length=50, blank=True, null=True)
    telefone = models.CharField(max_length=9, blank=True, null=True)
    celular = models.CharField(max_length=10, blank=True, null=True)
