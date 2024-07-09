# pip install pymysql -> si no tenemos instalada la dependencia
# importar pymysql para generar conexiones mysql sencillas con python

import pymysql

# conectar con el servidro MySQL
# conexión local
# def conectarMySQL():
#     host="localhost"
#     user="root"
#     password=""
#     database="borbocoders"
#     return pymysql.connect(host=host,user=user,password=password,database=database)

# conexión pythonanywhere
def conectarMySQL():
    host="ezequielzanetti83.mysql.pythonanywhere-services.com"
    user="ezequielzanetti8"
    password="codo2024"
    database="ezequielzanetti8$cac"
    return pymysql.connect(host=host,user=user,password=password,database=database)