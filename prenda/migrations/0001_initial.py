# Generated by Django 3.1.7 on 2021-05-03 03:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('referencia', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Prenda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_operacion', models.CharField(max_length=20, unique=True)),
                ('estado', models.CharField(max_length=20)),
                ('cant_total', models.IntegerField(blank=True, null=True)),
                ('cant_tallaS', models.IntegerField(blank=True, null=True)),
                ('cant_tallaM', models.IntegerField(blank=True, null=True)),
                ('cant_tallaL', models.IntegerField(blank=True, null=True)),
                ('cant_tallaXL', models.IntegerField(blank=True, null=True)),
                ('cant_tallaXXL', models.IntegerField(blank=True, null=True)),
                ('rS', models.IntegerField(blank=True, null=True)),
                ('rM', models.IntegerField(blank=True, null=True)),
                ('rL', models.IntegerField(blank=True, null=True)),
                ('rXL', models.IntegerField(blank=True, null=True)),
                ('rXXL', models.IntegerField(blank=True, null=True)),
                ('nota', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('referencia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Prenda', to='referencia.referencia')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Prenda', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['nom_operacion'],
            },
        ),
    ]
