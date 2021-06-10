from django import forms
from .models import Producto, Categoria

class ProductoForm(forms.ModelForm):
    
    class Meta:
        model = Producto
        fields= '__all__' #['id', 'codigoBarra', 'descripcion', 'precioCosto', 'precioVenta','activo', 'categoria']
 
class CategoriaForm(forms.ModelForm):
    
    class Meta:
        model = Categoria
        fields= '__all__' 