# PyMySQL reemplaza a mysqlclient como conector de Django con MySQL
try:
    import pymysql
    pymysql.install_as_MySQLdb()
except ImportError:
    pass
