from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render

from .models import Producto

# Create your views here.
# @login_required >> si el usuario no ha iniciado sesión, lo manda al login

def registrarUsuario(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '')
        password_confirm = request.POST.get('password_confirm', '')

        if not username or not password:
            return render(request, 'login.html', {
                'active_tab': 'register',
                'register_error': 'Por favor completa todos los campos requeridos.'
            })

        if password != password_confirm:
            return render(request, 'login.html', {
                'active_tab': 'register',
                'register_error': 'Las contraseñas no coinciden.',
                'reg_username': username
            })

        if User.objects.filter(username=username).exists():
            return render(request, 'login.html', {
                'active_tab': 'register',
                'register_error': f'El usuario "{username}" ya existe. Elige otro nombre.'
            })

        # Crear usuario utilizando el modelo auth de Django
        user = User.objects.create_user(username=username, password=password)
        login(request, user)
        messages.success(request, f'¡Cuenta creada exitosamente! Bienvenido, {username}.')
        return redirect('/')

    return render(request, 'login.html', {'active_tab': 'register'})

@login_required
def mostrarIndex(request):
    total_productos = Producto.objects.count()
    return render(request, 'index.html', {'total_productos': total_productos})

@login_required
def mostrarListado(request):
    productos = Producto.objects.all().order_by('id')
    return render(request, 'listado.html', {'productos': productos})

@login_required
def mostrarFormRegistrar(request):
    return render(request, 'form_registrar.html')

@login_required
def registrarProducto(request):
    if request.method == 'POST':
        nombre = request.POST.get('txtnom', '').strip()
        marca = request.POST.get('cbomar', '').strip()
        precio = request.POST.get('txtpre', '').strip()

        if nombre and marca and precio:
            Producto.objects.create(
                nombre=nombre,
                marca=marca,
                precio=int(precio),
            )
            messages.success(request, f'Producto "{nombre}" agregado con éxito.')
    return redirect('/listado')

@login_required
def mostrarFormActualizar(request, id):
    producto = get_object_or_404(Producto, id=id)
    return render(request, 'form_actualizar.html', {'producto': producto})

@login_required
def actualizarProducto(request, id):
    producto = get_object_or_404(Producto, id=id)
    if request.method == 'POST':
        producto.nombre = request.POST.get('txtnom', producto.nombre).strip()
        producto.marca = request.POST.get('cbomar', producto.marca).strip()
        precio = request.POST.get('txtpre')
        if precio:
            producto.precio = int(precio)
        producto.save()
        messages.success(request, f'Producto "#{producto.id}" actualizado correctamente.')
    return redirect('/listado')

@login_required
def eliminarProducto(request, id):
    producto = get_object_or_404(Producto, id=id)
    nombre = producto.nombre
    producto.delete()
    messages.success(request, f'Producto "{nombre}" eliminado con éxito.')
    return redirect('/listado')
