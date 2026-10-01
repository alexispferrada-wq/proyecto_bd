"""
Configuración principal de rutas (URLconf) del proyecto 'Proyecto_BD'.

Define el mapeo entre las URLs del navegador y las funciones de vista (views)
encargadas de procesar la solicitud y devolver la respuesta.
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path

from productos import views

urlpatterns = [
    # 1. Panel de Administración de Django
    path('admin/', admin.site.urls),

    # 2. Rutas de Autenticación y Control de Acceso (Etapa 1)
    # Vista genérica de Django para login usando nuestra plantilla personalizada
    path('login', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    # Cierre de sesión y redirección al formulario de login
    path('logout', auth_views.LogoutView.as_view(next_page='/login'), name='logout'),
    # Registro de nuevos usuarios en la base de datos
    path('registro', views.registrarUsuario, name='registro'),

    # 3. Menú Principal del Sistema
    path('', views.mostrarIndex, name='index'),

    # 4. Operaciones CRUD de Productos (Etapa 2 y 3)
    # CREATE: Mostrar formulario de registro y procesar guardado
    path('form_registrar', views.mostrarFormRegistrar, name='form_registrar'),
    path('registrar', views.registrarProducto, name='registrar'),

    # READ: Mostrar tabla con el listado de productos
    path('listado', views.mostrarListado, name='listado'),

    # UPDATE: Mostrar formulario de edición con datos cargados y guardar cambios
    path('form_actualizar/<int:id>', views.mostrarFormActualizar, name='form_actualizar'),
    path('actualizar/<int:id>', views.actualizarProducto, name='actualizar'),

    # DELETE: Eliminar un producto por su clave primaria (ID)
    path('eliminar/<int:id>', views.eliminarProducto, name='eliminar'),
]
