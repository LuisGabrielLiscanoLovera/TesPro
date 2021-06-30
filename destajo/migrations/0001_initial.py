# Generated by Django 3.1.7 on 2021-06-30 04:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('integrante', '0001_initial'),
        ('tarea', '0001_initial'),
        ('prenda', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Destajo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField(blank=True, null=True)),
                ('talla', models.CharField(blank=True, max_length=5, null=True)),
                ('can_resta', models.IntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('integrante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Destajo', to='integrante.integrante')),
                ('nom_operacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Destajo', to='prenda.prenda')),
                ('tarea', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Destajo', to='tarea.tarea')),
            ],
        ),
    ]
