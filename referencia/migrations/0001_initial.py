# Generated by Django 3.1.7 on 2021-07-07 00:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('empresa', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Referencia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_referencia', models.CharField(max_length=20, unique=True)),
                ('descripcion', models.CharField(max_length=50)),
                ('fotoPrendaUno', models.ImageField(blank=True, upload_to='uploads/')),
                ('fotoPrendaDos', models.ImageField(blank=True, upload_to='uploads/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('empresa', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Referencia', to='empresa.empresa')),
                ('usuario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Referencia', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.AddIndex(
            model_name='referencia',
            index=models.Index(fields=['created_at'], name='referencia__created_577b7e_idx'),
        ),
    ]
