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
        ('patinador', '0001_initial'),
        ('talla', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=140)),
                ('date', models.DateField(auto_now_add=True)),
                ('completed', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['completed', 'date'],
            },
        ),
        migrations.CreateModel(
            name='Despacho',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('can_terminada', models.IntegerField()),
                ('nomTallaDespacho', models.CharField(max_length=140)),
                ('nomPatinadorDespacho', models.CharField(max_length=140)),
                ('btnDelDespacho', models.CharField(blank=True, default='', max_length=300, null=True)),
                ('estatus', models.CharField(blank=True, choices=[('A', 'Activo'), ('I', 'Inactivo')], default='A', max_length=1, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empresa.empresa')),
                ('operacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='operacion.operacion')),
                ('patinador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patinador.patinador')),
                ('talla', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='talla.talla')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
