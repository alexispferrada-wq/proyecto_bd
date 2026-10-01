from django.db import models

# Create your models here.

class Producto(models.Model):
    nombre = models.TextField(max_length=100)
    marca = models.TextField(max_length=100)
    precio = models.IntegerField(null=False)

"""
Explicación:
- models.algo   >> le estamos indicando la características del atributo de la tabla de nuestra BD
- null=False    >> indica que es un dato obligatorio
- no se indica el id, el cual por defecto será creado
"""
