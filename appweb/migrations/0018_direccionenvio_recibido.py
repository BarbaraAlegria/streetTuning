# Generated by Django 4.2.1 on 2024-06-10 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appweb', '0017_alter_direccionenvio_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='direccionenvio',
            name='recibido',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
