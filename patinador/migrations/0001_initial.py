# Generated by Django 3.1.7 on 2022-02-18 23:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('empresa', '0001_initial'),
        ('integrante', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patinador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estatus', models.CharField(choices=[('A', 'Activo'), ('I', 'Inactivo')], max_length=1)),
                ('password', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('btnAcci', models.CharField(blank=True, default='<button type="button" class="btn btn-outline-warning text-center btn-sm btn-block ">Accion</button>', max_length=97, null=True)),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Patinador', to='empresa.empresa')),
                ('integrante', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='Patinador', to='integrante.integrante')),
                ('usuario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Patinador', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.AddIndex(
            model_name='patinador',
            index=models.Index(fields=['created_at'], name='patinador_p_created_0e7855_idx'),
        ),
    ]
