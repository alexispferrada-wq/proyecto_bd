# Proyecto_BD - Django con MySQL en Docker

Proyecto Django con base de datos MySQL 8.0 y phpMyAdmin completamente dockerizado.

## Requisitos previos

- [Docker](https://www.docker.com/) y Docker Compose instalados.

## Cómo levantar el proyecto en un nuevo entorno

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/alexispferrada-wq/proyecto_bd.git
   cd proyecto_bd
   ```

2. **Iniciar los contenedores:**
   ```bash
   docker compose up -d
   ```
   *(Docker construirá la imagen web, esperará que MySQL esté saludable y aplicará las migraciones automáticamente).*

3. **Accesos:**
   - **Aplicación Django:** [http://localhost:8000](http://localhost:8000)
   - **phpMyAdmin:** [http://localhost:8080](http://localhost:8080)
     - Servidor: `db`
     - Usuario root: `root` / Contraseña: `root123`
     - Usuario Django: `django` / Contraseña: `django123`
   - **Base de datos MySQL:** puerto local `3307` (`bd_productos`)

4. **Crear un superusuario (opcional):**
   ```bash
   docker compose exec web python manage.py createsuperuser
   ```

5. **Detener el entorno:**
   ```bash
   docker compose down
   ```
