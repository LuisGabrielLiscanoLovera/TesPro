# Generated by Django 4.0.5 on 2022-06-15 07:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Acumulado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('costeAcu', models.IntegerField(blank=True, default=0, null=True)),
                ('nom_acumulado', models.CharField(max_length=35, unique=True)),
                ('nota', models.CharField(blank=True, default='', max_length=150, null=True)),
                ('estatus', models.CharField(blank=True, choices=[('A', 'Activo'), ('I', 'Inactivo')], default='A', max_length=1, null=True)),
                ('btnAcci', models.CharField(default='<button type="button" class="btn btn-outline-warning text-center btn-sm btn-block ">Accion</button>', max_length=300, null=True)),
                ('delAcumulado', models.CharField(blank=True, default='', max_length=150, null=True)),
                ('btnInfo', models.CharField(default='<button type="button" class="btn btn-outline-info text-center btn-sm btn-block ">Info</button>', max_length=300, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('fecha_cierre', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='ProAcumulado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('can_prod_acum', models.IntegerField()),
                ('delAcumulProc', models.CharField(default='', max_length=200, null=True)),
                ('estatus', models.CharField(blank=True, choices=[('A', 'Activo'), ('I', 'Inactivo')], default='A', max_length=1, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('fecha_cierre', models.DateTimeField(blank=True, null=True)),
                ('acumulado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='acumulado.acumulado')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]
