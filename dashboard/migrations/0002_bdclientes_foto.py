# Generated by Django 2.2.5 on 2019-11-03 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bdclientes',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='fotos'),
        ),
    ]
