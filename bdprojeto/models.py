from django.db import models
from .forms import forms


class bdclientes(models.Model):

    id_cliente = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=30, blank=True, null=True)
    sobrenome = models.CharField(max_length=30, blank=True, null=True)
    cnpj = models.CharField(max_length=11, blank=False, null=True)
    celular = models.CharField(max_length=9, blank=True, null=True)
    email = models.CharField(max_length=254, blank=True, null=True)
    
    class Meta:
        ordering = ["nome"]
    