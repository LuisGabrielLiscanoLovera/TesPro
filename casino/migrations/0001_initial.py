# Generated by Django 3.1.7 on 2021-07-07 00:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('empresa', '0001_initial'),
        ('integrante', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Casino',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField(blank=True, null=True)),
                ('deuda', models.IntegerField(blank=True, default=0, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('btnInfo', models.CharField(blank=True, default='<button type="button" class="btn btn-outline-info icofont-info-square text-center btn-sm btn-block"></button>', max_length=1000, null=True)),
                ('btnAcci', models.CharField(blank=True, default='<button type="button" class="btn btn-outline-info icofont-dollar-true text-center btn-sm btn-block"></button>', max_length=1000, null=True)),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Casino', to='empresa.empresa')),
                ('integrante', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='Casino', to='integrante.integrante')),
                ('usuario', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='Casino', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.AddIndex(
            model_name='casino',
            index=models.Index(fields=['created_at'], name='casino_casi_created_00d07e_idx'),
        ),
    ]
