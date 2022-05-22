# Generated by Django 4.0.4 on 2022-05-20 22:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('talla', '0002_talla_estatus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cantalla',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='CanTalla', to=settings.AUTH_USER_MODEL),
        ),
    ]