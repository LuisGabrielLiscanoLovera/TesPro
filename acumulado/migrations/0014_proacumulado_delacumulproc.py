# Generated by Django 4.0.4 on 2022-05-23 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acumulado', '0013_proacumulado_tarea'),
    ]

    operations = [
        migrations.AddField(
            model_name='proacumulado',
            name='delAcumulProc',
            field=models.CharField(default='', max_length=150, null=True),
        ),
    ]
