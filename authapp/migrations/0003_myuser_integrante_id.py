# Generated by Django 4.0.4 on 2022-06-02 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0002_myuser_patinador'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='integrante_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
