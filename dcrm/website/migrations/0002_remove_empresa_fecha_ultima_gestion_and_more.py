# Generated by Django 4.2.1 on 2023-10-18 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='empresa',
            name='fecha_ultima_gestion',
        ),
        migrations.AddField(
            model_name='empresa',
            name='fecha_ultima_actualizacion',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]