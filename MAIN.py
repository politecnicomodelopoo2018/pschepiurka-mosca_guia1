from db import DB
from class_alumno import Alumno
from class_profesor import Profesor
from class_materia import Materia
from class_curso import Curso
import os

loop = True

while loop:
    os.system("clear")
    print("Bienvenido. Conecte el programa a una Base de Datos")
    host = input("HOST: ")
    user = input("USUARIO: ")
    passwd = input("CONTRASEÑA: ")
    db = input("NOMBRE DE LA BASE DE DATOS: ")
    DB().setConexion(host, user, passwd, db)

    os.system("clear")
    print("¿Con qué desea trabajar? \n"
          "1. Curso \n"
          "2. Profesor \n"
          "3. Alumno \n"
          "4. Materia \n")
    opcion = input("Opción: ")

    if int(opcion) == 1:
        list = DB().run("select * from Curso")
        print(list["idCurso"])
        input()