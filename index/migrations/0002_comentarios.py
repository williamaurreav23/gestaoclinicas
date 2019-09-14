# Generated by Django 2.2.5 on 2019-09-09 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='comentarios',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, max_length=30, null=True)),
                ('comentario', models.CharField(blank=True, max_length=100, null=True)),
                ('url', models.URLField(blank=True, max_length=30, null=True)),
            ],
            options={
                'ordering': ['nome'],
            },
        ),
    ]
