# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Ativos(models.Model):
    id_ativo = models.CharField(primary_key=True, max_length=-1)
    tipo_ativo = models.CharField(max_length=20, blank=True, null=True)
    descricao_passivo = models.CharField(max_length=20, blank=True, null=True)
    valor_ativo = models.IntegerField(blank=True, null=True)
    data_ativo = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ativos'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DashboardAtivos(models.Model):
    id_ativo = models.SmallIntegerField(blank=True, null=True)
    nome = models.SmallIntegerField(blank=True, null=True)
    valor = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dashboard_ativos'


class DashboardClientes(models.Model):
    nome = models.CharField(max_length=30, blank=True, null=True)
    sobrenome = models.CharField(max_length=30, blank=True, null=True)
    cnpj = models.CharField(max_length=11, blank=True, null=True)
    celular = models.CharField(max_length=9, blank=True, null=True)
    email = models.CharField(max_length=254, blank=True, null=True)
    foto = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dashboard_clientes'


class DashboardClinica(models.Model):
    clinica_id = models.AutoField(primary_key=True)
    nomefantasia = models.CharField(max_length=100)
    cnpj = models.CharField(unique=True, max_length=100)
    email = models.CharField(max_length=20, blank=True, null=True)
    contato = models.CharField(max_length=11, blank=True, null=True)
    especialidade = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dashboard_clinica'


class DashboardContatos(models.Model):
    nome = models.CharField(max_length=50, blank=True, null=True)
    sobrenome = models.CharField(max_length=50, blank=True, null=True)
    telefone = models.CharField(max_length=9, blank=True, null=True)
    celular = models.CharField(max_length=10, blank=True, null=True)
    id_cliente = models.ForeignKey('DashboardEmpresas', models.DO_NOTHING, db_col='id_cliente', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dashboard_contatos'


class DashboardEmpresas(models.Model):
    id_cliente = models.SmallIntegerField(primary_key=True)
    nome_fantasia = models.CharField(db_col='nome fantasia', max_length=50, blank=True,
                                     null=True)  # Field renamed to remove unsuitable characters.
    nome_juridico = models.CharField(db_col='nome juridico', max_length=50, blank=True,
                                     null=True)  # Field renamed to remove unsuitable characters.
    cnpj = models.CharField(max_length=11)

    class Meta:
        managed = False
        db_table = 'dashboard_empresas'


class DashboardFuncionario(models.Model):
    id_func = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    naturalidade_cid = models.CharField(max_length=20, blank=True, null=True)
    cor_raca = models.CharField(max_length=10, blank=True, null=True)
    data_nasc = models.DateField(blank=True, null=True)
    dependentes = models.IntegerField(blank=True, null=True)
    estado_civil = models.CharField(max_length=10, blank=True, null=True)
    mae = models.CharField(max_length=50, blank=True, null=True)
    nacionalidade = models.CharField(max_length=50, blank=True, null=True)
    naturalidade_estado = models.CharField(max_length=20, blank=True, null=True)
    pai = models.CharField(max_length=50, blank=True, null=True)
    sexo = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dashboard_funcionario'


class DashboardGestor(models.Model):
    gestor_id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    email = models.CharField(max_length=20, blank=True, null=True)
    celular = models.CharField(max_length=11, blank=True, null=True)
    especialidade = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dashboard_gestor'


class DashboardIndicadoresnegativos(models.Model):
    id = models.SmallIntegerField(primary_key=True)
    questao = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dashboard_indicadoresnegativos'


class DashboardLucratividade(models.Model):
    id = models.SmallIntegerField(primary_key=True)
    lucro_liquido_anual = models.SmallIntegerField(blank=True, null=True)
    receita_total_anual = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dashboard_lucratividade'


class DashboardPassivos(models.Model):
    id_passivo = models.SmallIntegerField(primary_key=True)
    nome = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dashboard_passivos'


class DashboardRoi(models.Model):
    id = models.SmallIntegerField(primary_key=True)
    receita = models.SmallIntegerField(blank=True, null=True)
    custo = models.SmallIntegerField(blank=True, null=True)
    item = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dashboard_roi'


class DashboardTaxaconversao(models.Model):
    visitantes = models.SmallIntegerField(primary_key=True)
    id = models.SmallIntegerField(blank=True, null=True)
    conversoes = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dashboard_taxaconversao'


class DashboardTicketmediovendas(models.Model):
    id = models.SmallIntegerField(primary_key=True)
    total_receita = models.SmallIntegerField(blank=True, null=True)
    total_vendas = models.SmallIntegerField(blank=True, null=True)
    nr_compras = models.SmallIntegerField(blank=True, null=True)
    periodo = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dashboard_ticketmediovendas'


class DashboardTurnover(models.Model):
    id = models.SmallIntegerField(primary_key=True)
    contratados = models.SmallIntegerField(blank=True, null=True)
    desligamentos = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dashboard_turnover'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoChatterbotStatement(models.Model):
    text = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    conversation = models.CharField(max_length=32)
    in_response_to = models.CharField(max_length=255, blank=True, null=True)
    persona = models.CharField(max_length=50)
    search_text = models.CharField(max_length=255)
    search_in_response_to = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'django_chatterbot_statement'


class DjangoChatterbotStatementTags(models.Model):
    statement = models.ForeignKey(DjangoChatterbotStatement, models.DO_NOTHING)
    tag = models.ForeignKey('DjangoChatterbotTag', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_chatterbot_statement_tags'
        unique_together = (('statement', 'tag'),)


class DjangoChatterbotTag(models.Model):
    name = models.CharField(unique=True, max_length=50)

    class Meta:
        managed = False
        db_table = 'django_chatterbot_tag'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Passivos(models.Model):
    id_passivo = models.CharField(primary_key=True, max_length=-1)
    tipo_passivo = models.CharField(max_length=20, blank=True, null=True)
    descricao_passivo = models.CharField(max_length=20, blank=True, null=True)
    valor_passivo = models.IntegerField(blank=True, null=True)
    data_passivo = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'passivos'
