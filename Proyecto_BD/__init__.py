"""
Inicialización del paquete del proyecto.

Configura PyMySQL como reemplazo compatible de mysqlclient para la conexión con MySQL
cuando se ejecute en Docker o con base de datos MySQL externa.
Si no está instalado (por ejemplo en entornos locales sólo con SQLite), continúa sin error.
"""
try:
    import pymysql
    pymysql.install_as_MySQLdb()
except ImportError:
    pass
