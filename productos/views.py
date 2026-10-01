from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .models import Producto

# Create your views here.
# @login_required >> si el usuario no ha iniciado sesión, lo manda al login

@login_required
def mostrarIndex(request):
    return render(request,'index.html')

@login_required
def mostrarListado(request):
    productos = Producto.objects.all().order_by('id')
    return render(request,'listado.html', {'productos': productos})

@login_required
def mostrarFormRegistrar(request):
    return render(request,'form_registrar.html')

@login_required
def registrarProducto(request):
    if request.method == 'POST':
        Producto.objects.create(
            nombre=request.POST['txtnom'],
            marca=request.POST['cbomar'],
            precio=request.POST['txtpre'],
        )
    return redirect('/listado')

@login_required
def mostrarFormActualizar(request, id):
    producto = get_object_or_404(Producto, id=id)
    return render(request,'form_actualizar.html', {'producto': producto})

@login_required
def actualizarProducto(request, id):
    producto = get_object_or_404(Producto, id=id)
    if request.method == 'POST':
        producto.nombre = request.POST['txtnom']
        producto.marca = request.POST['cbomar']
        producto.precio = request.POST['txtpre']
        producto.save()
    return redirect('/listado')

@login_required
def eliminarProducto(request, id):
    get_object_or_404(Producto, id=id).delete()
    return redirect('/listado')
