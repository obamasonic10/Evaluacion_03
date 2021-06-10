from django import forms
<<<<<<< HEAD
from .models import Producto, Categoria
=======
from .models import Producto, Categoria, Cliente, Pais, NivelEducacional
>>>>>>> 3b6ae540981a75c7907302d6ee3a516b84829584

class ProductoForm(forms.ModelForm):
    
    class Meta:
        model = Producto
        fields= '__all__' #['id', 'codigoBarra', 'descripcion', 'precioCosto', 'precioVenta','activo', 'categoria']
<<<<<<< HEAD
 
class CategoriaForm(forms.ModelForm):
    
    class Meta:
        model = Categoria
=======
 
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
>>>>>>> 3b6ae540981a75c7907302d6ee3a516b84829584
        fields= '__all__' 