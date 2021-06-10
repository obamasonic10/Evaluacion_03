from django.urls import path
from .views import inicio,normales, premium, listadoProducto, formProducto, formModProducto, eliminarProducto, crearCategoria, listarCategoria,modificarCategoria, eliminarCategoria




urlpatterns = [
    path('', inicio, name="inicio"),

    path('normales.html', normales, name="normales"),
    path('premium.html', premium, name="premium"),



    path('listadoProducto', listadoProducto, name="listadoProducto"),
    path('formProducto', formProducto, name="formProducto"),
    path('formModProducto/<id>', formModProducto, name="formModProducto"),
    path('eliminarProducto/<id>', eliminarProducto, name="eliminarProducto"),



    path('crearCategoria', crearCategoria, name="crearCategoria"),
    path('listarCategoria', listarCategoria, name="listarCategoria"),
    path('modificarCategoria/<id>', modificarCategoria, name="modificarCategoria"),
    path('eliminarCategoria/<id>', eliminarCategoria, name="eliminarCategoria"),

   
    ]