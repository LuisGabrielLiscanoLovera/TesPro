# Generated by Django 3.1.7 on 2021-07-11 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('talla', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='talla',
            name='btnAcci',
            field=models.CharField(blank=True, default='<button type="button" class="btn btn-outline-light text-center btn-sm btn-block ">Accion</button>', max_length=150, null=True),
        ),
    ]