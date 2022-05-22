# Generated by Django 4.0.4 on 2022-05-21 23:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0003_remove_relacionempresa_updated_at'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('acumulado', '0002_alter_acumulado_nom_acumulado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acumulado',
            name='empresa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empresa.empresa'),
        ),
        migrations.AlterField(
            model_name='acumulado',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]