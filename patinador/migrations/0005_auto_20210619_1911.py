# Generated by Django 3.1.7 on 2021-06-20 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patinador', '0004_remove_patinador_btninfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patinador',
            name='btnAcci',
            field=models.CharField(blank=True, default='<button type="button" class="btn btn-outline-light text-center btn-sm btn-block ">Accion</button>', max_length=97, null=True),
        ),
    ]
