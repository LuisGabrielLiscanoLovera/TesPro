# Generated by Django 4.0.5 on 2022-06-25 01:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('empresa', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tarea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_tarea', models.CharField(max_length=50)),
                ('min_minuto', models.IntegerField(blank=True, null=True)),
                ('min_hora', models.IntegerField(blank=True, null=True)),
                ('valor', models.IntegerField(blank=True, null=True)),
                ('detalle', models.CharField(blank=True, max_length=150, null=True)),
                ('btnInfo', models.CharField(default='<button type="button" class="btn    btn-outline-info text-center btn-sm btn-block">Info</button>', max_length=100)),
                ('btnAcci', models.CharField(default='<button type="button" class="btn btn-outline-warning text-center btn-sm btn-block ">Accion</button>', max_length=100)),
                ('estatus', models.CharField(blank=True, choices=[('A', 'Activo'), ('I', 'Inactivo')], default='A', max_length=1, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empresa.empresa')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
