# Generated by Django 4.2.1 on 2024-06-09 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appweb', '0013_rename_opion_opinion'),
    ]

    operations = [
        migrations.AddField(
            model_name='direccionenvio',
            name='Estado',
            field=models.CharField(default='Pendiente', max_length=50),
        ),
    ]
