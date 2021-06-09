from django.db import models

# Create your models here.
class Tipo(models.Model):
    id = models.IntegerField(primary_key = True)
    nombre = models.CharField(max_length=50)
    activo = models.BooleanField()

    def __str__(self):
    
        return self.nombre

class Producto (models.Model):
    id = models.IntegerField(primary_key = True)
    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE, verbose_name="Categoría")
    codigoBarra = models.IntegerField(verbose_name="Código de Barras")
    descripcion = models.CharField(max_length=50, verbose_name="Descripción")
    precioCosto = models.IntegerField(verbose_name="Precio Costo")
    precioVenta = models.IntegerField(verbose_name="Precio Venta")
    activo = models.BooleanField(verbose_name="Activo")
    

    def __str__(self):
        return self.descripcion