from django.urls import path
from .views import inicio, listarTipo, crearTipo,  modificarTipo, eliminarTipo

urlpatterns = [
    path('', inicio, name="inicio"),






    path('listarTipo', listarTipo, name="listarTipo"),
    path('crearTipo', crearTipo, name="crearTipo"),
    path('modificarTipo/<id>', modificarTipo, name="modificarTipo"),
    path('eliminarTipo/<id>', eliminarTipo, name="eliminarTipo"),
]