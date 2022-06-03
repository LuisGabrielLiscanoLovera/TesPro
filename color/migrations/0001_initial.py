# Generated by Django 4.0.4 on 2022-06-03 20:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('empresa', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_color', models.CharField(max_length=20)),
                ('codigo_color', models.CharField(blank=True, max_length=25, null=True)),
                ('estatus', models.CharField(blank=True, choices=[('A', 'Activo'), ('I', 'Inactivo')], default='A', max_length=1, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Color', to='empresa.empresa')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Color', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.AddIndex(
            model_name='color',
            index=models.Index(fields=['created_at'], name='color_color_created_7f800b_idx'),
        ),
    ]
