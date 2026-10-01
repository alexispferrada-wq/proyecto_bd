# Proyecto_BD - Django (Docker o Local)

Proyecto Django preparado para funcionar tanto con **Docker** (Django + MySQL + phpMyAdmin) como en **entorno local directo con Python** (SQLite o MySQL).

---

## 🚀 Opción 1: Ejecutar con Docker (Recomendado para producción/clon completo)

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

> **Nota para usar MySQL local sin Docker:**  
> Si tienes un MySQL instalado en tu máquina, copia `.env.example` a `.env` o define las variables `DB_HOST=localhost`, `DB_USER=...`, `DB_PASSWORD=...`, `DB_NAME=bd_productos`.
