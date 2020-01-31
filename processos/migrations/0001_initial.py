# Generated by Django 3.0.2 on 2020-01-24 15:05

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
            name='Despesa',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('receita_total', models.TextField(blank=True, null=True)),
                ('receita_total_anual', models.TextField(blank=True, null=True)),
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
                ('data_inicio', models.DateField(blank=True, null=True)),
                ('data_fim', models.DateField(blank=True, null=True)),
                ('investimento', models.DecimalField(decimal_places=2, max_digits=1000, null=True)),
                ('lucro_liquido', models.DecimalField(decimal_places=2, max_digits=1000, null=True)),
                ('rentabilidade', models.DecimalField(decimal_places=2, max_digits=1000, null=True)),
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
