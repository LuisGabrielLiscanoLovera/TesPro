# Generated by Django 4.0.4 on 2022-05-25 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acumulado', '0016_alter_proacumulado_delacumulproc'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='acumulado',
            name='can_total',
        ),
        migrations.AlterField(
            model_name='proacumulado',
            name='delAcumulProc',
            field=models.CharField(default='', max_length=200, null=True),
        ),
    ]
