# Generated by Django 4.0.5 on 2022-06-06 04:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('integrante', '0001_initial'),
        ('produccion', '0003_remove_produccion_costeprod'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produccion',
            name='integrante',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='integrante.integrante'),
        ),
    ]
