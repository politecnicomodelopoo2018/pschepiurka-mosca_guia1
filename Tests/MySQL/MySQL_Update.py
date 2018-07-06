import pymysql
#HACER UN UPDATE

#Conexion a la DB
db = pymysql.connect(host="localhost", user="root", passwd="alumno", charset="utf8",db = "mydb", autocommit=True)

#Creacion de Cursor
update_cursor = db.cursor()

#Hacemos el update
n = input()
update_cursor.execute("UPDATE Empleado SET nombre='A', apellido='B' WHERE idEmpleado=" + n + ";")

#Cerramos la conexion
db.close()

#En el caso en el que 'autocommit' no sea True, utilizamos update.cursor.commit() antes de cerrar la DB