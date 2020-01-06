from django.db import models


class Land(models.Model):
    nome_empresa = models.CharField(max_length=50, blank=True, null=True)
    nome_contato = models.CharField(max_length=50, blank=True, null=True)
    celular = models.CharField(max_length=10, blank=True, null=True)
    email = models.EmailField(max_length=254, blank=True, null=True)
    CONSULTORIA = 'CS'
    TREINAMENTO = 'TR'
    MARKETING = 'MK'
    OUTROS = 'OU'

    INTERESSE = [
        (CONSULTORIA, 'Consultoria'),
        (TREINAMENTO, 'Treinamento'),
        (MARKETING, 'Marketing'),
        (OUTROS, 'Outros'),
    ]

    interesse = models.CharField(
        max_length=2,
        choices=INTERESSE,
        default=CONSULTORIA,
    )
