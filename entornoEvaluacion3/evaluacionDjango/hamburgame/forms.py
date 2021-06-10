from django import forms
from .models import Producto, Categoria, Cliente, Pais, NivelEducacional

class ProductoForm(forms.ModelForm):
    
    class Meta:
        model = Producto
        fields= '__all__' #['id', 'codigoBarra', 'descripcion', 'precioCosto', 'precioVenta','activo', 'categoria']
 
class CategoriaForm(forms.ModelForm):
    
    class Meta:
        model = Categoria
        fields= '__all__' 
 
class ClienteForm(forms.ModelForm):
    
    class Meta:
        model = Cliente
        fields= '__all__' 

class PaisForm(forms.ModelForm):
    
    class Meta:
        model = Pais
        fields= '__all__' 

class NivelEducacional(forms.ModelForm):
    
    class Meta:
        model = NivelEducacional
        fields= '__all__' 