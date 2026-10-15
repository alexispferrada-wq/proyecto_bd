"""
Pruebas automatizadas para la API REST de 'productos'.
Valida los métodos HTTP: GET, POST, PUT, PATCH, DELETE usando Django REST Framework.
"""
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Producto


class ProductoAPITests(APITestCase):
    def setUp(self):
        self.producto = Producto.objects.create(
            nombre="Monitor 27 Pulgadas",
            marca="Samsung",
            precio=179990
        )
        self.list_url = "/productos/"
        self.detail_url = f"/productos/{self.producto.id}/"

    def test_get_productos_list(self):
        """GET /productos/ - Listar recursos"""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_post_producto_create(self):
        """POST /productos/ - Crear recurso"""
        payload = {
            "nombre": "Audífonos Bluetooth",
            "marca": "Sony",
            "precio": 89990
        }
        response = self.client.post(self.list_url, payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["nombre"], "Audífonos Bluetooth")

    def test_get_producto_detail(self):
        """GET /productos/{id}/ - Leer detalle de recurso"""
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["marca"], "Samsung")

    def test_put_producto_update(self):
        """PUT /productos/{id}/ - Actualizar recurso completo"""
        payload = {
            "nombre": "Monitor 32 Pulgadas 4K",
            "marca": "Samsung",
            "precio": 299990
        }
        response = self.client.put(self.detail_url, payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["nombre"], "Monitor 32 Pulgadas 4K")
        self.assertEqual(response.data["precio"], 299990)

    def test_patch_producto_partial_update(self):
        """PATCH /productos/{id}/ - Modificar parcialmente recurso"""
        payload = {"precio": 159990}
        response = self.client.patch(self.detail_url, payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["precio"], 159990)

    def test_delete_producto(self):
        """DELETE /productos/{id}/ - Eliminar recurso"""
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Producto.objects.filter(id=self.producto.id).exists())
