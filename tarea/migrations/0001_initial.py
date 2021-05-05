# Generated by Django 3.1.7 on 2021-05-04 05:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tarea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_tarea', models.CharField(max_length=20)),
                ('duracion', models.IntegerField(blank=True, null=True)),
                ('valor', models.IntegerField(blank=True, null=True)),
                ('min_hora', models.IntegerField(blank=True, null=True)),
                ('detalle', models.CharField(max_length=150)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Tarea', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
