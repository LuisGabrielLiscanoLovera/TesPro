# Generated by Django 3.1.7 on 2021-07-13 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operacion', '0008_auto_20210711_1807'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='operacion',
            options={'ordering': ['created_at']},
        ),
        migrations.AddField(
            model_name='operacion',
            name='btnInfo',
            field=models.CharField(blank=True, default='<button type="button" class="btn btn-outline-light text-center btn-sm btn-block ">Info</button>', max_length=300, null=True),
        ),
    ]