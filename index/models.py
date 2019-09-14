from django.db import models


class comentarios(models.Model):

    nome = models.CharField(max_length=30, blank=True, null=True)
    comentario =  models.CharField(max_length=100, blank=True, null=True)
    url = models.URLField(max_length=30, blank=True, null=True)


    class Meta:
        ordering = ["nome"]
