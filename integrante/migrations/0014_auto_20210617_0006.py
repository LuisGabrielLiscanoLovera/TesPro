# Generated by Django 3.1.7 on 2021-06-17 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('integrante', '0013_auto_20210617_0002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='integrante',
            name='btnAcci',
            field=models.CharField(blank=True, default='<button type="button" class="btn btn-outline-light text-center btn-sm btn-block ">Accion</button>', max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='integrante',
            name='btnInfo',
            field=models.CharField(blank=True, default='<button type="button" class="btn btn-outline-light text-center btn-sm btn-block">Info</button>', max_length=30, null=True),
        ),
    ]
