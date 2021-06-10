from django.shortcuts import render, redirect
from .models import Producto, Categoria, Cliente
from .forms import ProductoForm, CategoriaForm, ClienteForm
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





















def crearCliente(request):
    contexto = {'formulario' : ClienteForm }

## guardar en la base de datos --> modelos    
    if request.method == 'POST':
        formulario = ClienteForm(request.POST)
        formulario.save()
        contexto['mensaje'] = "Los datos fueron guardados"
        
    return render(request, 'crearCliente.html', contexto)

def listarCliente(request):
    listado = Cliente.objects.all() 

    if request.method == 'POST':
        buscar = request.POST['txtBuscar'] 
        listado = Cliente.objects.filter(nombre__contains = buscar).order_by('nombre', 'apellido')

    contexto = { 'listado' : listado  }
    return render(request, 'listarCliente.html', contexto)

def modificarCliente(request, id):
    objeto = Cliente.objects.get(id = id)
    contexto = {'form' : ClienteForm(instance=objeto) }

    if request.method == 'POST':
        formulario = ClienteForm(data=request.POST, instance=objeto)
        formulario.save()
        contexto['mensaje'] = "Los datos fueron guardados"
        contexto['form'] = ClienteForm(instance=Cliente.objects.get(id = id))

    return render(request, 'modificarCliente.html', contexto)


def eliminarCliente(request, id):
    objeto = Cliente.objects.get(id = id)
    objeto.delete()
    return redirect(to="listarCliente")





















