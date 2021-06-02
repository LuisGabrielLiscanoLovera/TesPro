# Generated by Django 3.1.7 on 2021-05-30 16:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('empresa', '0001_initial'),
        ('integrante', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patinador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estutus', models.CharField(choices=[('A', 'Activo'), ('I', 'Inactivo')], max_length=1)),
                ('password', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Patinador', to='empresa.empresa')),
                ('nom_patinador', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='Patinador', to='integrante.integrante')),
            ],
            options={
                'ordering': ['nom_patinador'],
            },
        ),
    ]
