# Generated by Django 3.1.7 on 2022-03-26 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operacion', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operacion',
            name='nom_operacion',
            field=models.CharField(max_length=35),
        ),
    ]
