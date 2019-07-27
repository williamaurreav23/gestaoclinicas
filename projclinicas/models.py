from django.db import models

# Create your models here.

class Gestor(models.Model):
    gestor_id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    email = models.CharField(max_length=20, blank=True, null=True)
    celular = models.CharField(max_length=11, blank=True, null=True)
    especialidade = models.CharField(max_length=30, blank=True, null=True)

class Funcionario(models.Model):
    funcionario_id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    email = models.CharField(max_length=20, blank=True, null=True)
    celular = models.CharField(max_length=11, blank=True, null=True)
    especialidade = models.CharField(max_length=30, blank=True, null=True)


class Clinica(models.Model):
    clinica_id = models.AutoField(primary_key=True)
    nomefantasia = models.CharField(max_length=100)
    cnpj = models.CharField(unique=True, max_length=100)
    email = models.CharField(max_length=20, blank=True, null=True)
    contato = models.CharField(max_length=11, blank=True, null=True)
    especialidade = models.CharField(max_length=30, blank=True, null=True)

class Cliente(models.Model):
    cliente_id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    email = models.CharField(max_length=20, blank=True, null=True)
    celular = models.CharField(max_length=11, blank=True, null=True)
    especialidade = models.CharField(max_length=30, blank=True, null=True)

