# Generated by Django 4.0.4 on 2022-05-16 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tarea', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tarea',
            name='estatus',
            field=models.CharField(choices=[('A', 'Activo'), ('I', 'Inactivo')], default='A', max_length=1),
        ),
    ]