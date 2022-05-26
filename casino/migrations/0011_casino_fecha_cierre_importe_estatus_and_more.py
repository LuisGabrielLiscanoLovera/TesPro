# Generated by Django 4.0.4 on 2022-05-26 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('casino', '0010_importe_delcasinoimport'),
    ]

    operations = [
        migrations.AddField(
            model_name='casino',
            name='fecha_cierre',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='importe',
            name='estatus',
            field=models.CharField(blank=True, choices=[('A', 'Activo'), ('I', 'Inactivo')], default='A', max_length=1, null=True),
        ),
        migrations.AddField(
            model_name='importe',
            name='fecha_cierre',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
