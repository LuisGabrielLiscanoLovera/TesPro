# Generated by Django 3.1.7 on 2021-07-11 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operacion', '0005_talla_num_talla'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operacion',
            name='btnAcci',
            field=models.CharField(blank=True, default='<button type="button" class="btn btn-outline-info icofont-dollar-true text-center btn-sm btn-block">btn</button>', max_length=300, null=True),
        ),
    ]
