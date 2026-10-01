"""
Configuración del panel de administración de Django para la app 'productos'.
Permite gestionar los productos visualmente desde /admin/.
"""
from django.contrib import admin
from .models import Producto

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    # Columnas que se mostrarán en la tabla del panel de administración
    list_display = ('id', 'nombre', 'marca', 'precio')
    
    # Campo de búsqueda rápida por nombre o marca
    search_fields = ('nombre', 'marca')
    
    # Filtro lateral por marca
    list_filter = ('marca',)
    
    # Orden predeterminado por ID ascendente
    ordering = ('id',)
