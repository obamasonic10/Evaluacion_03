from django.urls import path
from .views import inicio, crearTipo, listarTipo, modificarTipo, eliminarTipo

urlpatterns = [
    path('', inicio, name="inicio"),






    path('crearTipo', crearTipo, name="crearTipo"),
    path('listarTipo', listarTipo, name="listarTipo"),
    path('modificarTipo/<id>', modificarTipo, name="modificarTipo"),
    path('eliminarTipo/<id>', eliminarTipo, name="eliminarTipo"),
]