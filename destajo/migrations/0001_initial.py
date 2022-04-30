# Generated by Django 3.1.7 on 2022-04-30 01:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('integrante', '0001_initial'),
        ('tarea', '0001_initial'),
        ('empresa', '0001_initial'),
        ('operacion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Destajo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField(blank=True, null=True)),
                ('talla', models.CharField(blank=True, max_length=5, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='DestajoE', to='empresa.empresa')),
                ('integrante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Destajo', to='integrante.integrante')),
                ('operacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Destajo', to='operacion.operacion')),
                ('tarea', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Destajo', to='tarea.tarea')),
                ('usuario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Destajo', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
