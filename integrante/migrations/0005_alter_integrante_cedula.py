# Generated by Django 4.0.4 on 2022-05-28 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('integrante', '0004_alter_integrante_cedula'),
    ]

    operations = [
        migrations.AlterField(
            model_name='integrante',
            name='cedula',
            field=models.CharField(max_length=30),
        ),
    ]