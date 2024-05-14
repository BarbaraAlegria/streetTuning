# Generated by Django 4.2.1 on 2024-05-09 20:47

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('appweb', '0003_producto_foto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Personalizado',
            fields=[
                ('id_personalizado', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=4000)),
                ('apellido', models.CharField(max_length=4000)),
                ('telefono', models.IntegerField()),
                ('foto', models.ImageField(null=True, upload_to='sticker')),
                ('descripcion', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='producto',
            name='precio',
            field=models.IntegerField(),
        ),
    ]