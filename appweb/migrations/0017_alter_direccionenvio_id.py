# Generated by Django 4.2.1 on 2024-06-10 00:07

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('appweb', '0016_alter_direccionenvio_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='direccionenvio',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
