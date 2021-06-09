from django.shortcuts import render, redirect
from .models import Producto, Tipo
from .forms import ProductoForm, TipoForm
# Create your views here.
def inicio(request):
    return render(request, 'index.html')

def normales(request):
    return render(request, 'normales.html')    

def premium(request):
    return render(request, 'premium.html')       







































#TIPO
def listarTipo(request):
    tipos = Tipo.objects.all() 

    if request.method == 'POST':
        buscar = request.POST['txtBuscar']
        tipos = Tipo.objects.filter(nombre__contains = buscar).order_by('nombre') 

    contexto = { 'categorias' : tipos  }
    return render(request, 'listarTipo.html', contexto)
    
def crearTipo(request):
    contexto = {'formulario' : TipoForm }
  
    if request.method == 'POST':
        formulario = TipoForm(request.POST)
        formulario.save()
        contexto['mensaje'] = "Los datos fueron guardados"
        
    return render(request, 'crearTipo.html', contexto)

# agregar solo 1 vez : from .forms import CategoriaForm 
def modificarTipo(request, id):
    tipo = Tipo.objects.get(id = id)
    contexto = {'form' : TipoForm(instance=tipo) }

    if request.method == 'POST':
        formulario = TipoForm(data=request.POST, instance=tipo)
        formulario.save()
        contexto['mensaje'] = "Los datos fueron guardados"
        contexto['form'] = TipoForm(instance=Tipo.objects.get(id = id))

    return render(request, 'modificarTipo.html', contexto)

def eliminarTipo(request, id):
    tipo = Tipo.objects.get(id = id)

    tipo.delete()
    return redirect(to="listarTipo")
