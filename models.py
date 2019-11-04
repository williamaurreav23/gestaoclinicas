# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.


class DashboardBdclientes(models.Model):
    nome = models.CharField(max_length=30, blank=True, null=True)
    sobrenome = models.CharField(max_length=30, blank=True, null=True)
    cnpj = models.CharField(max_length=11, blank=True, null=True)
    celular = models.CharField(max_length=9, blank=True, null=True)
    email = models.CharField(max_length=254, blank=True, null=True)
    foto = models.CharField(max_length=100, blank=True, null=True)



class DashboardCliente(models.Model):
    cliente_id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    email = models.CharField(max_length=20, blank=True, null=True)
    celular = models.CharField(max_length=11, blank=True, null=True)
    especialidade = models.CharField(max_length=30, blank=True, null=True)



class DashboardClinica(models.Model):
    clinica_id = models.AutoField(primary_key=True)
    nomefantasia = models.CharField(max_length=100)
    cnpj = models.CharField(unique=True, max_length=100)
    email = models.CharField(max_length=20, blank=True, null=True)
    contato = models.CharField(max_length=11, blank=True, null=True)
    especialidade = models.CharField(max_length=30, blank=True, null=True)



class DashboardFuncionario(models.Model):
    funcionario_id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    email = models.CharField(max_length=20, blank=True, null=True)
    celular = models.CharField(max_length=11, blank=True, null=True)
    especialidade = models.CharField(max_length=30, blank=True, null=True)



class DashboardGestor(models.Model):
    gestor_id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    email = models.CharField(max_length=20, blank=True, null=True)
    celular = models.CharField(max_length=11, blank=True, null=True)
    especialidade = models.CharField(max_length=30, blank=True, null=True)
