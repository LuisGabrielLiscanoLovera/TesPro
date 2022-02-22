# Generated by Django 3.1.7 on 2022-02-22 05:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('talla', '0001_initial'),
        ('empresa', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('operacion', '0001_initial'),
        ('integrante', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Despacho',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('can_terminada', models.IntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='DespachoE', to='empresa.empresa')),
                ('nom_patinador', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='DespachoPP', to='integrante.integrante')),
                ('operacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='DespachoO', to='operacion.operacion')),
                ('talla', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='DespachoT', to='talla.talla')),
                ('usuario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Despacho', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
