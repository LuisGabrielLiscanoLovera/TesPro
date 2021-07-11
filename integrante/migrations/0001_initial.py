# Generated by Django 3.1.7 on 2021-07-11 00:48

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
            name='Integrante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estatus', models.CharField(choices=[('A', 'Activo'), ('I', 'Inactivo')], max_length=1)),
                ('nombres', models.CharField(max_length=30)),
                ('apellidos', models.CharField(max_length=30)),
                ('sexo', models.CharField(choices=[('H', 'Hombre'), ('M', 'Mujer'), ('O', 'Otro')], max_length=1)),
                ('correo', models.EmailField(max_length=254, verbose_name='Correo')),
                ('cedula', models.IntegerField(blank=True, null=True, unique=True)),
                ('num_telf', models.IntegerField(blank=True, null=True)),
                ('direccion', models.CharField(max_length=250)),
                ('abilidad', models.CharField(max_length=350)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('btnInfo', models.CharField(blank=True, default='<button type="button" class="btn btn-outline-light text-center btn-sm btn-block">Info</button>', max_length=100, null=True)),
                ('btnAcci', models.CharField(blank=True, default='<button type="button" class="btn btn-outline-light text-center btn-sm btn-block ">Accion</button>', max_length=100, null=True)),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Integrante', to='empresa.empresa')),
                ('usuario', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='Integrante', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['nombres'],
            },
        ),
    ]
