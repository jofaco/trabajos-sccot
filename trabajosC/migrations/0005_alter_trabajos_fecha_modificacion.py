# Generated by Django 4.0.4 on 2022-07-15 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trabajosC', '0004_alter_autores_celular'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trabajos',
            name='fecha_modificacion',
            field=models.DateField(blank=True, null=True, verbose_name='ultima modificacion'),
        ),
    ]
