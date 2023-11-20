# Generated by Django 4.2.1 on 2023-10-18 15:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_empleador', models.CharField(max_length=15)),
                ('fecha_ultima_gestion', models.DateTimeField(null=True)),
                ('razon_social', models.CharField(max_length=50, null=True)),
                ('celular', models.IntegerField(null=True)),
                ('telefono', models.IntegerField(null=True)),
                ('email', models.EmailField(max_length=50, null=True)),
                ('direccion', models.CharField(max_length=100, null=True)),
                ('comuna', models.CharField(max_length=50, null=True)),
                ('region', models.CharField(max_length=30, null=True)),
                ('cant_afiliados', models.PositiveIntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Gestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_hora', models.DateTimeField(auto_now_add=True)),
                ('tipo', models.CharField(max_length=20)),
                ('estado', models.CharField(max_length=20)),
                ('comentarios', models.TextField(null=True)),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.empresa')),
            ],
        ),
        migrations.CreateModel(
            name='Anotacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_alerta', models.CharField(max_length=20)),
                ('fecha_alerta', models.DateTimeField()),
                ('observacion', models.CharField(max_length=100)),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.empresa')),
            ],
        ),
    ]