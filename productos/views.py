"""
Vistas de la aplicación 'productos'.

Contiene la lógica de negocio para:
1. Autenticación y registro de usuarios en la base de datos.
2. Navegación en el menú principal del sistema.
3. Operaciones CRUD (Crear, Leer, Actualizar, Eliminar) sobre el modelo Producto.

Todas las vistas del sistema administrativo están protegidas con el decorador @login_required,
lo que garantiza que ningún usuario no autenticado pueda acceder o manipular datos.
"""
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render

from .models import Producto


# ==============================================================================
# 1. GESTIÓN DE AUTENTICACIÓN Y REGISTRO DE USUARIOS
# ==============================================================================

def registrarUsuario(request):
    """
    Gestiona el registro de nuevos usuarios en el sistema.
    - Si el usuario ya está autenticado, lo redirige al menú principal.
    - En peticiones POST: valida que las contraseñas coincidan y que el usuario no exista.
      Crea el usuario con User.objects.create_user(), inicia sesión y redirige al inicio.
    - En peticiones GET: renderiza la pestaña de registro en la plantilla 'login.html'.
    """
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '')
        password_confirm = request.POST.get('password_confirm', '')

        # Validación 1: Campos requeridos
        if not username or not password:
            return render(request, 'login.html', {
                'active_tab': 'register',
                'register_error': 'Por favor completa todos los campos requeridos.'
            })

        # Validación 2: Coincidencia de contraseñas
        if password != password_confirm:
            return render(request, 'login.html', {
                'active_tab': 'register',
                'register_error': 'Las contraseñas no coinciden.',
                'reg_username': username
            })

        # Validación 3: Nombre de usuario único
        if User.objects.filter(username=username).exists():
            return render(request, 'login.html', {
                'active_tab': 'register',
                'register_error': f'El usuario "{username}" ya existe. Elige otro nombre.'
            })

        # Creación del usuario con hash seguro de contraseña en la tabla auth_user
        user = User.objects.create_user(username=username, password=password)
        login(request, user)  # Inicia sesión automáticamente tras el registro
        messages.success(request, f'¡Cuenta creada exitosamente! Bienvenido, {username}.')
        return redirect('/')

    return render(request, 'login.html', {'active_tab': 'register'})


# ==============================================================================
# 2. VISTAS PRINCIPALES DEL SISTEMA (CRUD)
# ==============================================================================

@login_required
def mostrarIndex(request):
    """
    Muestra la pantalla principal (menú) del sistema.
    Calcula el total de productos registrados para mostrarlo como estadística en la interfaz.
    """
    total_productos = Producto.objects.count()
    return render(request, 'index.html', {'total_productos': total_productos})


@login_required
def mostrarListado(request):
    """
    [READ / CONSULTA]
    Obtiene todos los registros de la tabla Producto ordenados por ID de forma ascendente
    y los envía al template 'listado.html' para su visualización tabular.
    """
    productos = Producto.objects.all().order_by('id')
    return render(request, 'listado.html', {'productos': productos})


@login_required
def mostrarFormRegistrar(request):
    """
    [CREATE - FORMULARIO]
    Renderiza el formulario HTML vacío para ingresar un nuevo producto.
    """
    return render(request, 'form_registrar.html')


@login_required
def registrarProducto(request):
    """
    [CREATE - PROCESAMIENTO]
    Recibe los datos del formulario enviados por método POST y los inserta en la base de datos
    utilizando el método Producto.objects.create() del ORM de Django.
    """
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
            messages.success(request, f'Producto "{nombre}" agregado con éxito al catálogo.')
    return redirect('/listado')


@login_required
def mostrarFormActualizar(request, id):
    """
    [UPDATE - FORMULARIO]
    Busca el producto por su clave primaria (ID) utilizando get_object_or_404.
    Si no existe devuelve un error 404. Si existe, renderiza el formulario con los datos cargados.
    """
    producto = get_object_or_404(Producto, id=id)
    return render(request, 'form_actualizar.html', {'producto': producto})


@login_required
def actualizarProducto(request, id):
    """
    [UPDATE - PROCESAMIENTO]
    Recibe los datos editados por método POST, actualiza los atributos del objeto Producto
    y guarda los cambios persistentes en la base de datos mediante el método .save().
    """
    producto = get_object_or_404(Producto, id=id)
    if request.method == 'POST':
        producto.nombre = request.POST.get('txtnom', producto.nombre).strip()
        producto.marca = request.POST.get('cbomar', producto.marca).strip()
        precio = request.POST.get('txtpre')
        if precio:
            producto.precio = int(precio)
        producto.save()
        messages.success(request, f'Producto #{producto.id} actualizado correctamente.')
    return redirect('/listado')


@login_required
def eliminarProducto(request, id):
    """
    [DELETE - ELIMINACIÓN]
    Obtiene el producto por su ID y ejecuta el método .delete() del ORM para removerlo
    permanentemente de la base de datos. Luego redirige al listado actualizado.
    """
    producto = get_object_or_404(Producto, id=id)
    nombre = producto.nombre
    producto.delete()
    messages.success(request, f'Producto "{nombre}" eliminado con éxito.')
    return redirect('/listado')
