# Generated by Django 4.2.1 on 2024-05-21 17:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appweb', '0005_carritocompra_alter_cliente_usuario_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='carritocompra',
            old_name='created_at',
            new_name='creado_en',
        ),
        migrations.RenameField(
            model_name='carritocompra',
            old_name='id_carrito',
            new_name='id',
        ),
    ]
