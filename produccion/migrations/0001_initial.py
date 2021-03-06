# Generated by Django 4.0.5 on 2022-06-25 01:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('empresa', '0001_initial'),
        ('operacion', '0001_initial'),
        ('integrante', '0001_initial'),
        ('patinador', '0001_initial'),
        ('talla', '0001_initial'),
        ('tarea', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Produccion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('can_terminada', models.IntegerField()),
                ('delProduccion', models.CharField(default='', max_length=200, null=True)),
                ('estatus', models.CharField(blank=True, choices=[('A', 'Activo'), ('I', 'Inactivo')], default='A', max_length=1, null=True)),
                ('fecha_cierre', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empresa.empresa')),
                ('integrante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='integrante.integrante')),
                ('operacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='operacion.operacion')),
                ('patinador', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='patinador.patinador')),
                ('talla', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='ProduccionTallaFK', to='talla.talla')),
                ('tarea', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='tarea.tarea')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
