# Generated by Django 3.1.7 on 2021-07-11 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operacion', '0004_auto_20210710_2019'),
    ]

    operations = [
        migrations.AddField(
            model_name='talla',
            name='num_talla',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
