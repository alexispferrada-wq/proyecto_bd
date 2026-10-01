# GUÍA DE ESTUDIO E INTERROGACIÓN DE CÓDIGO
**Evaluación Sumativa N° 2 (35%) — Programación Back End**  
**INACAP Sede Maipú · Primavera 2026**

- **Docente:** Javier Eduardo Gutiérrez Osorio
- **Estudiante:** Alexis Ferrada
- **Puntaje Interrogación:** 30 puntos
- **Proyecto:** `Proyecto_BD` (Django 5.2 + MySQL / SQLite + Docker)
- **Documento PDF oficial:** `GUIA_ESTUDIO_INTERROGACION.pdf` (incluido en la raíz del proyecto)

---

## 1. Arquitectura General del Proyecto (Patrón MVT)

Django utiliza la arquitectura **MVT (Model - View - Template)**:
1. **Modelo (`models.py`):** Define las tablas y sus campos a través de clases en Python. El ORM de Django traduce estas clases a sentencias SQL en la base de datos sin escribir SQL manual.
2. **Vista (`views.py`):** Contiene la lógica de negocio. Recibe una solicitud HTTP (`request`), consulta o manipula los modelos y devuelve una respuesta HTTP (renderizando un template o redirigiendo).
3. **Plantilla (`templates/*.html`):** La interfaz visual en HTML con Bootstrap 5, variables (`{{ }}`) y estructuras de control (`{% %}`).
4. **Enrutador (`urls.py`):** Mapea cada URL escrita en el navegador con su correspondiente función de vista.

> **Flujo de Petición:**  
> Navegador ➔ `urls.py` ➔ `views.py` (con `@login_required`) ➔ `models.py (ORM)` ➔ Base de Datos ➔ Template HTML ➔ Respuesta al Navegador.

---

## 2. Explicación Detallada por Archivo

### 📄 `Proyecto_BD/settings.py` (Cerebro de Configuración)
- `INSTALLED_APPS`: Registra las aplicaciones del sistema. Se incluye `'productos'` junto a los módulos de autenticación (`django.contrib.auth`) y mensajes (`django.contrib.messages`).
- `DATABASES` (Soporte Dual):
  - **Sin Docker:** Si no detecta `DB_HOST`, usa **SQLite3** (`db.sqlite3`). Ideal para desarrollo rápido y lo sugerido en la guía de INACAP.
  - **Con Docker:** Al ejecutar `docker compose up`, inyecta `DB_HOST=db` y se conecta al contenedor de **MySQL 8.0**.
- `LOGIN_URL = '/login'`: Si un usuario intenta acceder a una ruta protegida sin iniciar sesión, Django lo envía a `/login`.
- `LANGUAGE_CODE = 'es-cl'` y `TIME_ZONE = 'America/Santiago'`: Localización chilena.

### 📄 `Proyecto_BD/urls.py` (Enrutamiento del Sistema)
Define la lista `urlpatterns`:
- `/login`: Vista genérica `LoginView` que renderiza `login.html`.
- `/logout`: Vista genérica `LogoutView` que cierra sesión y redirige a `/login`.
- `/registro`: Lógica personalizada para dar de alta usuarios en la tabla `auth_user`.
- `/`: Menú principal del sistema (`mostrarIndex`).
- `/form_registrar`: Formulario para crear un producto.
- `/registrar`: Procesa el guardado por método POST.
- `/listado`: Tabla con todos los productos registrados.
- `/form_actualizar/<int:id>`: Formulario de edición con datos cargados por ID.
- `/actualizar/<int:id>`: Procesa la edición por POST.
- `/eliminar/<int:id>`: Elimina el registro por su clave primaria.

### 📄 `productos/models.py` (Capa de Datos y ORM)
```python
class Producto(models.Model):
    nombre = models.TextField(max_length=100)
    marca = models.TextField(max_length=100)
    precio = models.IntegerField(null=False)
```
- Hereda de `models.Model`, lo que habilita los métodos del ORM (`.objects.all()`, `.create()`, `.get()`, etc.).
- Django crea automáticamente la columna `id` como clave primaria autoincrementable.
- Los 4 atributos corresponden exactamente a lo solicitado en la Etapa 2: ID, NOMBRE, MARCA y PRECIO.

### 📄 `productos/views.py` (Lógica de Negocio y Controladores)
- **`@login_required`:** Decorador colocado sobre cada función del CRUD. Verifica si el usuario inició sesión antes de permitir el acceso.
- **`registrarUsuario(request)`:** En peticiones POST valida que las contraseñas coincidan y que el usuario no exista. Crea el usuario con `User.objects.create_user()` (encriptando la clave con hash PBKDF2), inicia la sesión con `login(request, user)` y redirige al inicio.
- **`mostrarListado(request)`:** Ejecuta `Producto.objects.all().order_by('id')` y lo envía al template en `{'productos': productos}`.
- **`registrarProducto(request)`:** Captura los datos enviados por POST (`request.POST.get('txtnom')`, etc.) e inserta el registro con `Producto.objects.create(...)`.
- **`mostrarFormActualizar(request, id)`:** Busca el producto mediante `get_object_or_404(Producto, id=id)` y renderiza el formulario con sus datos actuales.
- **`actualizarProducto(request, id)`:** Actualiza los atributos del objeto y persiste los cambios con `producto.save()`.
- **`eliminarProducto(request, id)`:** Busca el registro y lo borra con `producto.delete()`.

### 📄 `productos/templates/` (Plantillas y Seguridad)
- **`{% csrf_token %}`:** Token de seguridad obligatorio en formularios POST que previene ataques de Cross-Site Request Forgery.
- **Diseño Centrado con Bootstrap 5:** Clases `d-flex align-items-center justify-content-center min-vh-100` para centrar vertical y horizontalmente las tarjetas en pantalla.
- **Confirmación en JavaScript:** Función `botonEliminar(id, nombre)` que utiliza `window.confirm()` antes de redirigir a `/eliminar/<id>`.

---

## 3. Simulacro de Interrogación (10 Preguntas Clave del Docente)

1. **¿Qué es el ORM y para qué sirve?**  
   *R:* Es el mapeador objeto-relacional de Django. Permite interactuar con la base de datos usando clases y métodos de Python (`Producto.objects.all()`), abstrayendo el código SQL y protegiendo contra inyecciones SQL.

2. **¿Cómo protegiste que nadie entre al CRUD sin logearse?**  
   *R:* Aplicando el decorador `@login_required` arriba de cada función de vista en `views.py`. Si alguien intenta entrar sin sesión, Django lo envía automáticamente a `/login`.

3. **¿Para qué sirve `{% csrf_token %}`?**  
   *R:* Genera un token criptográfico único en cada formulario POST para evitar ataques de falsificación de petición en sitios cruzados (CSRF).

4. **¿Diferencia entre `render()` y `redirect()`?**  
   *R:* `render()` procesa un HTML con variables de contexto y responde en la misma petición. `redirect()` envía un código HTTP 302 para ordenar al navegador solicitar una nueva URL (usado tras guardar o borrar para evitar reenvíos accidentales).

5. **¿Qué hace `get_object_or_404`?**  
   *R:* Busca un registro en la base de datos por su ID; si no existe, devuelve un error 404 controlado en lugar de tirar el servidor con una excepción no manejada.

6. **¿Cómo se guardan las contraseñas en la base de datos?**  
   *R:* Usando `User.objects.create_user()`, que aplica automáticamente un hash criptográfico PBKDF2 con SHA-256. Nunca se almacenan en texto plano.

7. **¿Qué son las migraciones?**  
   *R:* Son archivos Python en `migrations/` que registran la evolución del esquema de la base de datos. `makemigrations` prepara el archivo y `migrate` aplica los cambios en el motor de BD.

8. **¿Cómo soporta el proyecto tanto Docker como SQLite local?**  
   *R:* En `settings.py` se condiciona la configuración de `DATABASES`. Si detecta `DB_HOST` usa MySQL (Docker); si no, activa SQLite3 automáticamente sin requerir configuración adicional.

9. **¿Cómo se vinculan los contenedores de Docker?**  
   *R:* A través de la red interna de Docker Compose, usando el hostname `db` en el puerto 3306, con un healthcheck en MySQL para que Django espere a que la base de datos esté lista.

10. **¿Por qué se usa POST y no GET para crear productos?**  
    *R:* Porque POST está diseñado para operaciones que alteran el estado del servidor y la base de datos, evitando que datos sensibles o modificaciones queden expuestos en la URL o en el historial.
