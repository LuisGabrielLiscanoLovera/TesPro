# Generated by Django 4.0.5 on 2022-06-29 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('despacho', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='despacho',
            name='btnTareaSeg',
            field=models.CharField(blank=True, default='', max_length=300, null=True),
        ),
    ]
