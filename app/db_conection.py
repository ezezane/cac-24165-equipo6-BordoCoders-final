# pip install pymysql -> si no tenemos instalada la dependencia
# importar pymysql para generar conexiones mysql sencillas con python

import pymysql

# conectar con el servidro MySQL
def conectarMySQL():
    host="localhost"
    user="root"
    password=""
    database="borbocoders"
    return pymysql.connect(host=host,user=user,password=password,database=database)
