# Generated by Django 4.0.4 on 2022-05-22 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acumulado', '0009_acumulado_nota'),
    ]

    operations = [
        migrations.AddField(
            model_name='acumulado',
            name='delAcumulado',
            field=models.CharField(default='', max_length=150, null=True),
        ),
    ]