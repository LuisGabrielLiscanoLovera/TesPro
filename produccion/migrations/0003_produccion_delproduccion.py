# Generated by Django 4.0.4 on 2022-05-15 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produccion', '0002_alter_produccion_integrante'),
    ]

    operations = [
        migrations.AddField(
            model_name='produccion',
            name='delProduccion',
            field=models.CharField(default='', max_length=150, null=True),
        ),
    ]
