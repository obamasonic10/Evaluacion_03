from django.shortcuts import render, redirect
from .models import Producto, Categoria
from .forms import ProductoForm, CategoriaForm
# Create your views here.
def inicio(request):
    return render(request, 'index.html')

def normales(request):
    return render(request, 'normales.html')    

def premium(request):
    return render(request, 'premium.html')   

        
def listadoProducto(request):
# obtiene todos los datos de la tabla producto
    productos = Producto.objects.all()

    if request.method == 'POST':
        buscar = request.POST['txtBuscar']
        productos = Producto.objects.filter(descripcion__contains = buscar).order_by('descripcion') # select * from Categoria where nombre like '%patron%'
# crear el contexto para ser enviado a la plantilla (render)
    contexto = { 'productos' : productos  }
# renderizar (unir los datos con la plantilla)
    return render(request, 'listadoProducto.html', contexto)
    
def formProducto(request):
    contexto = {'form' : ProductoForm }

## guardar en la base de datos --> modelos    
    if request.method == 'POST':
        formulario = ProductoForm(request.POST)
        formulario.save()
        contexto['mensaje'] = "Los datos fueron guardados"
        
    return render(request, 'formProducto.html', contexto)


def formModProducto(request, id):
    producto = Producto.objects.get(id = id)
    contexto = {'form' : ProductoForm(instance=producto) }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto)
        formulario.save()
        contexto['mensaje'] = "Los datos fueron guardados"
        contexto['form'] = ProductoForm(instance=Producto.objects.get(id = id))

    return render(request, 'formModProducto.html', contexto)

def eliminarProducto(request, id):
    producto = Producto.objects.get(id = id)
# elimina el elemento de la base de datos
    producto.delete()
    return redirect(to="listadoProducto")














def listarCategoria(request):
# obtiene todos los datos de la tabla Categoria
    categorias = Categoria.objects.all() # select * from Categoria
#Ejercicios: aplicar filtro por descripción en Producto
    if request.method == 'POST':
        buscar = request.POST['txtBuscar'] ## startswith endswith
        categorias = Categoria.objects.filter(nombre__contains = buscar).order_by('activo', 'nombre') # select * from Categoria where nombre like '%patron%'

# crear el contexto para ser enviado a la plantilla (render)
    contexto = { 'categorias' : categorias  }
# renderizar (unir los datos con la plantilla)
    return render(request, 'listarCategoria.html', contexto)
    


def crearCategoria(request):
    contexto = {'formulario' : CategoriaForm }

## guardar en la base de datos --> modelos    
    if request.method == 'POST':
        formulario = CategoriaForm(request.POST)
        formulario.save()
        contexto['mensaje'] = "Los datos fueron guardados"
        
    return render(request, 'crearCategoria.html', contexto)

def modificarCategoria(request, id):
    categoria = Categoria.objects.get(id = id)
    contexto = {'form' : CategoriaForm(instance=categoria) }

    if request.method == 'POST':
        formulario = CategoriaForm(data=request.POST, instance=categoria)
        formulario.save()
        contexto['mensaje'] = "Los datos fueron guardados"
        contexto['form'] = CategoriaForm(instance=Categoria.objects.get(id = id))

    return render(request, 'modificarCategoria.html', contexto)


def eliminarCategoria(request, id):
    categoria = Categoria.objects.get(id = id)
# elimina el elemento de la base de datos
    categoria.delete()
    return redirect(to="listarCategoria")































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
