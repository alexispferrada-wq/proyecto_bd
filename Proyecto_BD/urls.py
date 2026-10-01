"""
URL configuration for Proyecto_BD project.
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path

from productos import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout', auth_views.LogoutView.as_view(next_page='/login'), name='logout'),
    path('registro', views.registrarUsuario, name='registro'),
    path('', views.mostrarIndex, name='index'),
    path('form_registrar', views.mostrarFormRegistrar, name='form_registrar'),
    path('registrar', views.registrarProducto, name='registrar'),
    path('listado', views.mostrarListado, name='listado'),
    path('form_actualizar/<int:id>', views.mostrarFormActualizar, name='form_actualizar'),
    path('actualizar/<int:id>', views.actualizarProducto, name='actualizar'),
    path('eliminar/<int:id>', views.eliminarProducto, name='eliminar'),
]
