# Generated by Django 4.1.6 on 2023-02-09 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AlmacenApp', '0002_movimientos_cantidad_alter_productos_en_almacen_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='productos',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to=None),
        ),
    ]
