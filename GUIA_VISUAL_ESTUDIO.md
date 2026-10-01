---
marp: true
theme: gaia
_class: lead
paginate: true
backgroundColor: #ffffff
color: #212529
style: |
  section {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    padding: 30px 40px;
  }
  h1 {
    color: #0b3d91;
    font-size: 1.8rem;
    margin-bottom: 0.2rem;
  }
  h2 {
    color: #0d6efd;
    font-size: 1.35rem;
    border-bottom: 2px solid #0d6efd;
    padding-bottom: 6px;
    margin-top: 0;
    margin-bottom: 12px;
  }
  p, li {
    font-size: 0.82rem;
    line-height: 1.45;
  }
  .card-box {
    background: #f8f9fa;
    border-left: 4px solid #0d6efd;
    border-radius: 6px;
    padding: 8px 14px;
    margin-bottom: 10px;
    font-size: 0.8rem;
  }
  .flex-container {
    display: flex;
    gap: 20px;
    align-items: center;
  }
  .flex-col {
    flex: 1;
  }
  .diagram-img {
    max-height: 420px;
    max-width: 100%;
    object-fit: contain;
    display: block;
    margin: 0 auto;
    border: 1px solid #dee2e6;
    border-radius: 8px;
    background: #ffffff;
    box-shadow: 0 4px 12px rgba(0,0,0,0.06);
  }
  .badge {
    display: inline-block;
    padding: 2px 8px;
    border-radius: 4px;
    font-weight: bold;
    font-size: 0.75rem;
    color: #fff;
    background: #0d6efd;
  }
---

<!-- _class: lead -->
# 🗺️ GUÍA VISUAL DE ESTUDIO
### Evaluación Sumativa N° 2 (35%) · Programación Back End
**INACAP Sede Maipú · Primavera 2026**

<div style="margin-top: 30px; font-size: 0.95rem; line-height: 1.8;">
  👤 <b>Estudiante:</b> Alexis Ferrada<br>
  👨‍🏫 <b>Docente:</b> Javier Eduardo Gutiérrez Osorio<br>
  🎯 <b>Puntaje Interrogación:</b> 30 Puntos (Explicación del Código)<br>
  📦 <b>Proyecto:</b> <code>Proyecto_BD</code> (Django 5.2 + MySQL / SQLite + Docker)
</div>

---

## 1. Ciclo de Vida de una Petición (Arquitectura MVT)

<div class="card-box">
  <b>¿Cómo viaja la información?</b> El usuario solicita una URL ➔ <code>urls.py</code> deriva a <code>views.py</code> ➔ <code>@login_required</code> valida sesión ➔ El ORM consulta a la Base de Datos ➔ La vista inyecta los datos en el Template HTML ➔ Se muestra en pantalla.
</div>

<img src="diagramas/01_mvt_flujo.svg" class="diagram-img" style="max-height: 380px;">

---

## 2. Estructura de la Base de Datos (Diagrama Entidad-Relación)

<div class="card-box">
  <b>Dos tablas principales:</b> <code>auth_user</code> (creada automáticamente para autenticación y login) y <code>productos_producto</code> (creada con el modelo Producto para el CRUD).
</div>

<img src="diagramas/02_entidad_relacion.svg" class="diagram-img" style="max-height: 380px;">

---

## 3. Diagrama de Clases y Controladores (UML)

<div class="card-box">
  <b>Estructura de Objetos:</b> <code>Producto</code> define los datos y se registra en <code>ProductoAdmin</code>. Las vistas funcionales controlan las operaciones CRUD llamando al ORM de Django.
</div>

<img src="diagramas/03_clases_uml.svg" class="diagram-img" style="max-height: 380px;">

---

## 4. Mapa Mental de Navegación (Sitemap de Pantallas)

<div class="card-box">
  <b>Flujo de usuario:</b> La pantalla principal unifica Login y Registro ➔ Al ingresar entra al Menú Principal ➔ Desde allí se accede a Registrar Producto o Listado ➔ Editar y Eliminar retornan siempre al Listado.
</div>

<img src="diagramas/04_mapa_navegacion.svg" class="diagram-img" style="max-height: 380px;">

---

## 5. Arquitectura de Despliegue: Docker vs Modo Local

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-top: 15px;">

<div style="background: #e7f5ff; border: 2px solid #339af0; border-radius: 8px; padding: 18px;">
  <h3 style="color: #1864ab; margin-top: 0; font-size: 1.1rem;">🐳 Modalidad Docker Compose</h3>
  <ul>
    <li><b>Contenedor Web (:8000):</b> Django 5.2 sobre Python 3.12.</li>
    <li><b>Contenedor BD (:3307):</b> Servidor MySQL 8.0 con healthcheck.</li>
    <li><b>Contenedor phpMyAdmin (:8080):</b> Interfaz visual de gestión.</li>
    <li><b>Volumen persistente:</b> <code>mysql_data</code> guarda los datos aunque se apague el contenedor.</li>
    <li><b>Red interna:</b> Los servicios se comunican usando el nombre de host <code>db:3306</code>.</li>
  </ul>
</div>

<div style="background: #ebfbee; border: 2px solid #40c057; border-radius: 8px; padding: 18px;">
  <h3 style="color: #2b8a3e; margin-top: 0; font-size: 1.1rem;">💻 Modalidad Local (Sin Docker)</h3>
  <ul>
    <li><b>Motor:</b> SQLite3 (archivo <code>db.sqlite3</code>).</li>
    <li><b>Recomendado en la pauta:</b> No requiere instalar MySQL ni encender servicios adicionales.</li>
    <li><b>Activación automática:</b> Si no existe la variable <code>DB_HOST</code>, Django activa SQLite de forma transparente.</li>
    <li><b>Comando directo:</b>
      <code>python manage.py migrate</code><br>
      <code>python manage.py runserver</code>
    </li>
  </ul>
</div>

</div>

---

## 6. Tarjeta Rápida para la Interrogación (30 Puntos)

<div style="font-size: 0.8rem; line-height: 1.5;">

| Pregunta del Profesor | Respuesta Exacta y Concisa |
| :--- | :--- |
| **¿Qué es el ORM?** | El mapeador de objetos de Django. Traduce clases y métodos Python (<code>.all()</code>, <code>.create()</code>, <code>.delete()</code>) a SQL sin escribir consultas a mano y previene inyecciones SQL. |
| **¿Cómo se protegen las rutas?** | Con el decorador <code>@login_required</code> arriba de cada vista. Si el usuario no tiene sesión activa, lo envía a <code>/login</code>. |
| **¿Para qué sirve <code>{% csrf_token %}</code>?** | Protege los formularios POST contra falsificación de petición en sitios cruzados mediante un token criptográfico único. |
| **¿Diferencia entre <code>render</code> y <code>redirect</code>?** | <code>render()</code> procesa y muestra un template HTML en la misma petición; <code>redirect()</code> responde con un código HTTP 302 hacia otra URL. |
| **¿Cómo se guardan las contraseñas?** | Con <code>User.objects.create_user()</code>, aplicando hash PBKDF2 con SHA-256. Nunca en texto plano. |

</div>

<div class="card-box" style="margin-top: 15px; text-align: center; border-left: none; border: 1px solid #198754; background: #ebfbee;">
  ✅ <b>¡Éxito en tu interrogación, Alexis! Toda la arquitectura está respaldada en este repositorio.</b>
</div>
