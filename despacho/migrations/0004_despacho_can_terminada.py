# Generated by Django 3.1.7 on 2022-03-27 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('despacho', '0003_remove_despacho_can_terminada'),
    ]

    operations = [
        migrations.AddField(
            model_name='despacho',
            name='can_terminada',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
