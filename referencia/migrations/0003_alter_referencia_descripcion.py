# Generated by Django 4.0.4 on 2022-05-24 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('referencia', '0002_referencia_fecha_cierre_alter_referencia_estatus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='referencia',
            name='descripcion',
            field=models.CharField(max_length=150),
        ),
    ]
