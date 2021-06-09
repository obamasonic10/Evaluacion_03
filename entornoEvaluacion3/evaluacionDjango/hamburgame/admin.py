from django.contrib import admin
from .models import Producto, Tipo
# Register your models here.

admin.site.register(Tipo)
admin.site.register(Producto)