# Generated by Django 4.0.4 on 2022-05-15 18:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('operacion', '0001_initial'),
        ('tarea', '0001_initial'),
        ('integrante', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('empresa', '0001_initial'),
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
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Destajo', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
