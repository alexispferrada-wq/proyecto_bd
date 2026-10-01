# Proyecto_BD - Django (Docker o Local)
**Evaluación Sumativa N° 2 (35%) — Programación Back End (INACAP Sede Maipú)**

Proyecto Django preparado para funcionar tanto con **Docker** (Django + MySQL + phpMyAdmin) como en **entorno local directo con Python** (SQLite o MySQL).

---

## 📚 Material de Estudio para la Interrogación (30 Puntos)

Para preparar la interrogación oral con el docente, en este mismo repositorio se incluye:
- **📄 [GUIA_ESTUDIO_INTERROGACION.pdf](GUIA_ESTUDIO_INTERROGACION.pdf)** *(Documento PDF listo para imprimir o descargar)*
- **📝 [GUIA_ESTUDIO_INTERROGACION.md](GUIA_ESTUDIO_INTERROGACION.md)** *(Versión en Markdown para lectura rápida en GitHub)*

Contiene el desglose archivo por archivo (`settings.py`, `urls.py`, `models.py`, `views.py`), arquitectura MVT, seguridad (CSRF y `@login_required`) y un **simulacro con las 10 preguntas clave del docente**.

---

## 🚀 Opción 1: Ejecutar con Docker (Django + MySQL + phpMyAdmin)

Incluye Python/Django, base de datos MySQL 8.0 y phpMyAdmin.

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/alexispferrada-wq/proyecto_bd.git
   cd proyecto_bd
   ```

2. **Levantar los servicios:**
   ```bash
   docker compose up -d
   ```
   *(Aplica migraciones automáticamente al iniciar el contenedor).*

3. **Accesos:**
   - **Django Web:** [http://localhost:8000](http://localhost:8000)
   - **phpMyAdmin:** [http://localhost:8080](http://localhost:8080)
     - Servidor: `db`
     - Usuario root: `root` / Contraseña: `root123`
     - Usuario Django: `django` / Contraseña: `django123`
   - **MySQL:** puerto local `3307`

4. **Crear superusuario (opcional):**
   ```bash
   docker compose exec web python manage.py createsuperuser
   ```

5. **Detener contenedores:**
   ```bash
   docker compose down
   ```

---

## 💻 Opción 2: Ejecutar SIN Docker (Entorno Local Python)

Si no tienes Docker instalado o prefieres correrlo directamente en tu máquina con SQLite:

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/alexispferrada-wq/proyecto_bd.git
   cd proyecto_bd
   ```

2. **Crear y activar entorno virtual:**
   - En macOS / Linux:
     ```bash
     python3 -m venv .venv
     source .venv/bin/activate
     ```
   - En Windows (PowerShell):
     ```powershell
     python -m venv .venv
     .venv\Scripts\Activate.ps1
     ```

3. **Instalar dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Ejecutar migraciones:**
   ```bash
   python manage.py migrate
   ```
   *(Por defecto usará SQLite `db.sqlite3` automáticamente si no defines `DB_HOST`).*

5. **Iniciar el servidor de desarrollo:**
   ```bash
   python manage.py runserver
   ```
   Disponible en: [http://127.0.0.1:8000](http://127.0.0.1:8000)
