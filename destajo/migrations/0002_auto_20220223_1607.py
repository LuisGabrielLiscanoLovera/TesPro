# Generated by Django 3.1.7 on 2022-02-23 21:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('destajo', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='destajo',
            old_name='nom_operacion',
            new_name='operacion',
        ),
    ]
