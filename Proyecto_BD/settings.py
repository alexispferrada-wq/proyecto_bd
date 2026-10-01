"""
Configuración general del proyecto 'Proyecto_BD'.

Generado con Django 5.2.17.
Configurado para soportar:
- Ejecución en contenedores Docker (MySQL 8.0 + phpMyAdmin)
- Ejecución directa local (SQLite3 integrada)
"""
import os
from pathlib import Path

# Directorio base del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent

# Clave secreta para propósitos de desarrollo (en producción debe protegerse en variables de entorno)
SECRET_KEY = 'django-insecure-*ewmo*%)jws0v*!rq5a2d4=mrl(wtlk^%=8p7%4**5bz5vbd2k'

# Modo depuración activo para desarrollo
DEBUG = True

# Permitir conexiones desde cualquier host local o contenedor
ALLOWED_HOSTS = ['*']


# ==============================================================================
# APLICACIONES INSTALADAS
# ==============================================================================
INSTALLED_APPS = [
    # Aplicaciones nativas de Django
    'django.contrib.admin',
    'django.contrib.auth',           # Sistema de autenticación de usuarios (auth_user)
    'django.contrib.contenttypes',
    'django.contrib.sessions',       # Manejo de sesiones de usuario
    'django.contrib.messages',       # Framework de notificaciones flash (mensajes)
    'django.contrib.staticfiles',
    # Aplicación propia del proyecto
    'productos',                     # CRUD y lógica de negocio de productos
]


# ==============================================================================
# MIDDLEWARE
# ==============================================================================
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',             # Protección contra ataques CSRF
    'django.contrib.auth.middleware.AuthenticationMiddleware', # Vincula request.user
    'django.contrib.messages.middleware.MessageMiddleware',    # Habilita framework de mensajes
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Proyecto_BD.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True, # Busca automáticamente carpetas 'templates' dentro de cada app
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'Proyecto_BD.wsgi.application'


# ==============================================================================
# BASE DE DATOS (SOPORTE DUAL: DOCKER / MYSQL Y LOCAL / SQLITE)
# ==============================================================================
USE_SQLITE = os.environ.get("USE_SQLITE", "").lower() in ("1", "true", "yes")
DB_HOST = os.environ.get("DB_HOST")

if USE_SQLITE or not DB_HOST:
    # Modalidad Local Simple (SQLite3)
    # Recomendado en la guía de INACAP: no requiere instalar ni iniciar MySQL
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }
else:
    # Modalidad Docker / MySQL
    # Se activa automáticamente al levantar con docker-compose (DB_HOST=db)
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.mysql",
            "NAME": os.environ.get("DB_NAME", "bd_productos"),
            "USER": os.environ.get("DB_USER", "django"),
            "PASSWORD": os.environ.get("DB_PASSWORD", "django123"),
            "HOST": DB_HOST,
            "PORT": os.environ.get("DB_PORT", "3306"),
            "OPTIONS": {"charset": "utf8mb4"},
        }
    }


# ==============================================================================
# VALIDACIÓN DE CONTRASEÑAS
# ==============================================================================
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]


# ==============================================================================
# INTERNACIONALIZACIÓN Y ZONA HORARIA (CHILE)
# ==============================================================================
LANGUAGE_CODE = 'es-cl'
TIME_ZONE = 'America/Santiago'
USE_I18N = True
USE_TZ = True


# ==============================================================================
# ARCHIVOS ESTÁTICOS Y CLAVES PRIMARIAS
# ==============================================================================
STATIC_URL = 'static/'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# ==============================================================================
# CONFIGURACIÓN DE AUTENTICACIÓN Y REDIRECCIONES (ETAPA 1 Y 3)
# ==============================================================================
LOGIN_URL = '/login'              # Redirección cuando un usuario no autenticado intenta entrar
LOGIN_REDIRECT_URL = '/'          # Destino al iniciar sesión correctamente
LOGOUT_REDIRECT_URL = '/login'     # Destino al cerrar sesión
