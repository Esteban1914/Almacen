# Generated by Django 4.1.6 on 2023-02-09 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AlmacenApp', '0004_alter_productos_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productos',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='AlmacenApp/Media'),
        ),
    ]
