from django.db import models

class Categoria(models.Model):
    id = models.IntegerField(primary_key = True)
    nombre = models.CharField(max_length=50)
    activo = models.BooleanField()

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    id          = models.IntegerField(primary_key = True)    
    categoria   = models.ForeignKey(Categoria, on_delete=models.CASCADE, verbose_name="Categoría")
    codigoBarra = models.IntegerField(verbose_name="Código de Barras")
    descripcion = models.CharField(max_length=50, verbose_name="Descripción")
    precioCosto = models.IntegerField(verbose_name="Precio Costo")
    precioVenta = models.IntegerField(verbose_name="Precio Venta")
    activo      = models.BooleanField(verbose_name="Activo")

    def __str__(self):
        return self.descripcion


class Pais(models.Model):
    id = models.IntegerField(primary_key = True)
    nombre_pais = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre_pais


class NivelEducacional(models.Model):
    id = models.IntegerField(primary_key = True)
    nivel = models.CharField(max_length=50)

    def __str__(self):
        return self.nivel


class Cliente(models.Model):
    id          = models.IntegerField(primary_key = True)
    rut         = models.CharField(max_length=50)
    nombre      = models.CharField(max_length=50)
    apellido    = models.CharField(max_length=50)
    correo      = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField(auto_now=False, auto_now_add=False)
    telefono = models.IntegerField()
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE, verbose_name="Pais")
    nivel_educacional = models.ForeignKey(NivelEducacional, on_delete=models.CASCADE, verbose_name="NivelEducacional")
    
    def __str__(self):
        return self.nombre + ' ' + self.apellido



