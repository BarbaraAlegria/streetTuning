# Generated by Django 4.2.1 on 2024-06-17 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appweb', '0025_remove_valoracion_usuario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),
                ('review', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Valoracion',
        ),
    ]
