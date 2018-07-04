import pymysql

#INGRESAR DATOS

#Conexion a la DB
db = pymysql.connect(host="localhost", user="root", passwd="alumno", db="mydb", charset="utf8", autocommit=True)

#Creacion del Cursor
cursor = db.cursor(pymysql.cursors.DictCursor)

#Ejecutamos la sentencia del Insert
cursor.execute("insert into Empleado values(NULL, 'Pepito', 'Sarasa')")

#Cerramos la conexion
db.close()