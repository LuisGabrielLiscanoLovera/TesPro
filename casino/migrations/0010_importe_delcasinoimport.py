# Generated by Django 4.0.4 on 2022-05-25 00:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('casino', '0009_remove_importe_estatus'),
    ]

    operations = [
        migrations.AddField(
            model_name='importe',
            name='delCasinoImport',
            field=models.CharField(default='', max_length=300, null=True),
        ),
    ]