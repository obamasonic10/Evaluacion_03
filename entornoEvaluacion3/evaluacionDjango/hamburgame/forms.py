from django import forms
from .models import Producto, Tipo

class ProductoForm(forms.ModelForm):
    
    class Meta:
        model = Producto
        fields= '__all__' 
 
class TipoForm(forms.ModelForm):
    
    class Meta:
        model = Tipo
        fields= '__all__' 