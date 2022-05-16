# Generated by Django 4.0.4 on 2022-05-16 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produccion', '0003_produccion_delproduccion'),
    ]

    operations = [
        migrations.AddField(
            model_name='produccion',
            name='estatus',
            field=models.CharField(blank=True, choices=[('A', 'Activo'), ('I', 'Inactivo')], default='A', max_length=1, null=True),
        ),
        migrations.AddField(
            model_name='produccion',
            name='fecha_cierre',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]