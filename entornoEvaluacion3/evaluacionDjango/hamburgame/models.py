from django.db import models

# Create your models here.
class Producto (models.Model):
    id = models.IntegerField(primary_key = True)
    codigoBarra = models.IntegerField(verbose_name="Código de Barras")
    descripcion = models.CharField(max_length=50, verbose_name="Descripción")
    precioCosto = models.IntegerField(verbose_name="Precio Costo")
    precioVenta = models.IntegerField(verbose_name="Precio Venta")
    tipo = models.IntegerField(verbose_name="Tipo")
    activo = models.BooleanField(verbose_name="Activo")