# Generated by Django 3.0.2 on 2020-01-17 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ativos',
            fields=[
                ('id_ativo', models.AutoField(primary_key=True, serialize=False)),
                ('tipo_ativo', models.CharField(blank=True, max_length=20, null=True)),
                ('descricao_ativo', models.CharField(blank=True, max_length=20, null=True)),
                ('valor_ativo', models.IntegerField(blank=True, null=True)),
                ('data_ativo', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(blank=True, max_length=30, null=True)),
                ('sobrenome', models.CharField(blank=True, max_length=30, null=True)),
                ('cnpj', models.CharField(max_length=11, null=True)),
                ('celular', models.CharField(blank=True, max_length=9, null=True)),
                ('email', models.CharField(blank=True, max_length=254, null=True)),
                ('foto', models.ImageField(blank=True, null=True, upload_to='fotos')),
            ],
            options={
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='Clinica',
            fields=[
                ('clinica_id', models.AutoField(primary_key=True, serialize=False)),
                ('nomefantasia', models.CharField(max_length=100)),
                ('cnpj', models.CharField(max_length=100, unique=True)),
                ('email', models.CharField(blank=True, max_length=20, null=True)),
                ('contato', models.CharField(blank=True, max_length=11, null=True)),
                ('especialidade', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contatos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, max_length=50, null=True)),
                ('sobrenome', models.CharField(blank=True, max_length=50, null=True)),
                ('telefone', models.CharField(blank=True, max_length=9, null=True)),
                ('celular', models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Despesa',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('receita_total', models.TextField(blank=True, null=True)),
                ('receita_total_anual', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Empresas',
            fields=[
                ('id_cliente', models.AutoField(primary_key=True, serialize=False)),
                ('nome_fantasia', models.CharField(blank=True, db_column='nome fantasia', max_length=50, null=True)),
                ('nome_juridico', models.CharField(blank=True, db_column='nome juridico', max_length=50, null=True)),
                ('cnpj', models.CharField(max_length=11)),
            ],
        ),
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id_func', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(blank=True, max_length=100, null=True)),
                ('nacionalidade', models.CharField(blank=True, max_length=50, null=True)),
                ('naturalidade_cid', models.CharField(blank=True, max_length=20, null=True)),
                ('naturalidade_estado', models.CharField(blank=True, max_length=20, null=True)),
                ('data_nasc', models.DateField(blank=True, null=True)),
                ('sexo', models.CharField(blank=True, max_length=10, null=True)),
                ('estado_civil', models.CharField(blank=True, max_length=10, null=True)),
                ('mae', models.CharField(blank=True, max_length=50, null=True)),
                ('pai', models.CharField(blank=True, max_length=50, null=True)),
                ('cor_raca', models.CharField(blank=True, max_length=10, null=True)),
                ('dependentes', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Gestor',
            fields=[
                ('gestor_id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=100)),
                ('email', models.CharField(blank=True, max_length=20, null=True)),
                ('celular', models.CharField(blank=True, max_length=11, null=True)),
                ('especialidade', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='IndicadoresNegativos',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('questao', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Lucratividade',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('lucro_liquido_anual', models.TextField(blank=True, null=True)),
                ('receita_total_anual', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Passivos',
            fields=[
                ('id_passivo', models.AutoField(primary_key=True, serialize=False)),
                ('tipo_passivo', models.CharField(blank=True, max_length=20, null=True)),
                ('descricao_passivo', models.CharField(blank=True, max_length=20, null=True)),
                ('valor_passivo', models.IntegerField(blank=True, null=True)),
                ('data_passivo', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Receita',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('receita_total', models.TextField(blank=True, null=True)),
                ('receita_total_anual', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Rentabilidade',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ano', models.DateField(blank=True, null=True)),
                ('mes', models.CharField(choices=[('JAN', 'JAN'), ('FEV', 'FEV'), ('MAR', 'MAR'), ('ABR', 'ABR'), ('MAI', 'MAI'), ('JUN', 'JUN'), ('JUL', 'JUL'), ('AGO', 'AGO'), ('SET', 'SET'), ('OUT', 'OUT'), ('NOV', 'NOV'), ('DEZ', 'DEZ')], default='JAN', max_length=3)),
                ('investimento', models.DecimalField(decimal_places=2, max_digits=1000, null=True)),
                ('lucro_liquido', models.DecimalField(decimal_places=2, max_digits=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Roi',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('receita', models.TextField(blank=True, null=True)),
                ('custo', models.TextField(blank=True, null=True)),
                ('item', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TaxaConversao',
            fields=[
                ('visitantes', models.AutoField(primary_key=True, serialize=False)),
                ('id', models.TextField(blank=True, null=True)),
                ('conversoes', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TicketMedioVendas',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('total_receita', models.TextField(blank=True, null=True)),
                ('total_vendas', models.TextField(blank=True, null=True)),
                ('nr_compras', models.TextField(blank=True, null=True)),
                ('periodo', models.DateField(blank=True, null=True)),
            ],
        ),
    ]
