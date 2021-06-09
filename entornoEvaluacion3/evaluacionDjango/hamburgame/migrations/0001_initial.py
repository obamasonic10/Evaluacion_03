# Generated by Django 3.2.4 on 2021-06-09 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('codigoBarra', models.IntegerField(verbose_name='Código de Barras')),
                ('descripcion', models.CharField(max_length=50, verbose_name='Descripción')),
                ('precioCosto', models.IntegerField(verbose_name='Precio Costo')),
                ('precioVenta', models.IntegerField(verbose_name='Precio Venta')),
                ('tipo', models.IntegerField(verbose_name='Tipo')),
                ('activo', models.BooleanField(verbose_name='Activo')),
            ],
        ),
    ]