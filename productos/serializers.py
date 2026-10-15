"""
Serializadores para la aplicación 'productos'.

Permite convertir instancias del modelo Producto a tipos de datos nativos de Python
que luego pueden renderizarse fácilmente a JSON, XML u otros tipos de contenido,
y deserializar datos validados de vuelta a objetos del modelo.
"""
from rest_framework import serializers

from .models import Producto


class ProductoSerializer(serializers.ModelSerializer):
    """
    Serializador que mapea automáticamente los campos del modelo Producto.
    Campos expuestos: id, nombre, marca, precio.
    """
    class Meta:
        model = Producto
        fields = '__all__'
