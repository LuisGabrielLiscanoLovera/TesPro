# Generated by Django 3.1.7 on 2022-05-02 02:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('color', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('referencia', '0001_initial'),
        ('empresa', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Operacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_operacion', models.CharField(max_length=35)),
                ('nota', models.CharField(blank=True, max_length=50, null=True)),
                ('estatus', models.CharField(choices=[('A', 'Activo'), ('I', 'Inactivo')], max_length=1)),
                ('can_total', models.IntegerField(blank=True, null=True)),
                ('can_restante', models.IntegerField(blank=True, null=True)),
                ('btnAcci', models.CharField(blank=True, default='<button type="button" class="btn btn-outline-warning text-center btn-sm btn-block ">Accion</button>', max_length=300, null=True)),
                ('btnInfo', models.CharField(blank=True, default='<button type="button" class="btn btn-outline-info text-center btn-sm btn-block ">Info</button>', max_length=300, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Operacion', to='color.color')),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Operacion', to='empresa.empresa')),
                ('referencia', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Operacion', to='referencia.referencia')),
                ('usuario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Operacion', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['created_at'],
            },
        ),
        migrations.AddIndex(
            model_name='operacion',
            index=models.Index(fields=['created_at'], name='operacion_o_created_6f3881_idx'),
        ),
    ]
