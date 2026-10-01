"""
Definición de modelos de la base de datos para la aplicación 'productos'.
Django utiliza este modelo para mapear la tabla en la base de datos mediante su ORM.
"""
from django.db import models


class Producto(models.Model):
    """
    Representa un producto dentro del sistema.
    Django crea automáticamente la columna 'id' como clave primaria autoincrementable.
    """
    nombre = models.TextField(max_length=100)
    marca = models.TextField(max_length=100)
    precio = models.IntegerField(null=False)

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        ordering = ['id']

    def __str__(self):
        return f"{self.nombre} ({self.marca}) - ${self.precio}"
