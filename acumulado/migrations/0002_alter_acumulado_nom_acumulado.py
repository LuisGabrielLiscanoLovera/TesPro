# Generated by Django 4.0.4 on 2022-05-21 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acumulado', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acumulado',
            name='nom_acumulado',
            field=models.CharField(max_length=35, unique=True),
        ),
    ]