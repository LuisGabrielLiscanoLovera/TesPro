# Generated by Django 3.1.7 on 2021-07-07 00:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_empresa', models.CharField(max_length=30)),
                ('direccion', models.CharField(max_length=150)),
                ('descripcion', models.CharField(max_length=100)),
                ('logo_empresa', models.ImageField(null=True, upload_to='uploads/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Empresa', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['nom_empresa'],
            },
        ),
        migrations.CreateModel(
            name='RelacionEmpresa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('Empresa', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='RelacionEmpresa', to='empresa.empresa')),
                ('Usuario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='RelacionEmpresa', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='CambioEmpres',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lastEm', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('Usuario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='CambioEmpres', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
