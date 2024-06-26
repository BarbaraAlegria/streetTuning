# Generated by Django 4.2.1 on 2024-05-08 23:29

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('rut', models.CharField(max_length=10)),
                ('nombre', models.CharField(max_length=80)),
                ('apellido', models.CharField(max_length=80)),
                ('usuario', models.IntegerField()),
                ('contraseña', models.BooleanField()),
                ('direccion', models.CharField(max_length=80)),
            ],
        ),
    ]
