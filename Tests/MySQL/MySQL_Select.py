import pymysql

#PRINTEAR DATOS

#Conectar a la base
db = pymysql.connect(host="127.0.0.1", user="root", passwd="alumno", db="mydb", autocommit=True)

#Abrimos el cursor.
#Si no aclaramos nada dentro de los parentesis, devuelve una lista
#PERO, si queremos que sea un diccionario, debemos usar la siguiente sintaxis:
cursor = db.cursor(pymysql.cursors.DictCursor)

#Seleccionamos los datos correspondientes
cursor.execute("select nombre, apellido from Empleado;")

#Printeamos los datos pedidos. La variable 'cursor' es un diccionario.
for line in cursor:
    print("Nombre: " + line["nombre"] + " " + "Apellido: " + line["apellido"])