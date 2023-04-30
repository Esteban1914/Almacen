# Generated by Django 4.1.7 on 2023-04-30 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StickersApp', '0005_product_pair_profit_worker'),
    ]

    operations = [
        migrations.CreateModel(
            name='SummaryDate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField(blank=True, null=True)),
                ('end_date', models.DateTimeField(blank=True, null=True)),
                ('active', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='movement',
            name='extra_info_int_2',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, default='no_user_imagen.jpg', null=True, upload_to='usuarios'),
        ),
        migrations.AlterField(
            model_name='movement',
            name='type',
            field=models.CharField(choices=[('AD', 'Agregado de Dinero'), ('EP', 'Agregado de Productos'), ('CM', 'Cierre de Mes'), ('cP', 'Confirmado de Producto'), ('CP', 'Creado de Producto'), ('eP', 'Editado de Producto'), ('eU', 'Editado de Usuario'), ('SP', 'Quitado de Productos'), ('rP', 'Reembolso de Productos'), ('RP', 'Removido de Producto'), ('RD', 'Retiro de Dinero'), ('VP', 'Venta de Productos')], max_length=2),
        ),
    ]
