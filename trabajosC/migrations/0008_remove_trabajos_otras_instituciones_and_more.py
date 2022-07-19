# Generated by Django 4.0.4 on 2022-07-18 13:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trabajosC', '0007_alter_trabajos_otros_autores'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trabajos',
            name='otras_instituciones',
        ),
        migrations.RemoveField(
            model_name='trabajos',
            name='otros_autores',
        ),
        migrations.AlterField(
            model_name='trabajos',
            name='Autor_correspondencia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trabajosC.autores'),
        ),
        migrations.AlterField(
            model_name='trabajos_has_autores',
            name='autor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='trabajosC.autores'),
        ),
        migrations.AlterField(
            model_name='trabajos_has_autores',
            name='trabajo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='trabajosC.trabajos'),
        ),
        migrations.CreateModel(
            name='Trabajos_has_instituciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institucion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='trabajosC.instituciones')),
                ('trabajo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='trabajosC.trabajos')),
            ],
        ),
    ]
