# Generated by Django 3.1.7 on 2022-02-22 05:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('empresa', '0001_initial'),
        ('operacion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Talla',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_talla', models.CharField(max_length=10)),
                ('num_talla', models.IntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('btnAcci', models.CharField(blank=True, default='<button type="button" class="btn btn-outline-warning text-center btn-sm btn-block ">Accion</button>', max_length=150, null=True)),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Talla', to='empresa.empresa')),
                ('usuario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Talla', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['created_at'],
            },
        ),
        migrations.CreateModel(
            name='CanTalla',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('can_talla', models.IntegerField(blank=True, null=True)),
                ('res_talla', models.IntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='CanTalla', to='empresa.empresa')),
                ('operacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='CanTalla', to='operacion.operacion')),
                ('talla', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='CanTalla', to='talla.talla')),
                ('usuario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='CanTalla', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['created_at'],
            },
        ),
        migrations.AddIndex(
            model_name='talla',
            index=models.Index(fields=['created_at'], name='talla_talla_created_f87627_idx'),
        ),
        migrations.AddIndex(
            model_name='cantalla',
            index=models.Index(fields=['created_at'], name='talla_canta_created_e08e0e_idx'),
        ),
    ]
