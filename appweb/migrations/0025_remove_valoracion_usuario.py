# Generated by Django 4.2.1 on 2024-06-15 01:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appweb', '0024_valoracion_delete_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='valoracion',
            name='usuario',
        ),
    ]