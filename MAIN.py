from db import DB
from class_alumno import Alumno
from class_profesor import Profesor
from class_materia import Materia
from class_curso import Curso
import os

loop = True

os.system("clear")
print("Bienvenido. Conecte el programa a una Base de Datos")
host = input("HOST: ")
user = input("USUARIO: ")
passwd = input("CONTRASEÑA: ")
db = input("NOMBRE DE LA BASE DE DATOS: ")
DB().setConexion(host, user, passwd, db)

while loop:
    os.system("clear")
    print("¿Con qué desea trabajar? \n"
          "1. Curso \n"
          "2. Profesor \n"
          "3. Alumno \n"
          "4. Materia \n")
    opcion = input("Opción: ")

    if int(opcion) == 1:
        os.system("clear")
        print("¿Que desea hacer con Curso?: \n")
        print("1. Crear Curso")
        print("2. Editar Curso")
        print("3. Eliminar Curso")
        print("4. Mostrar Cursos \n")
        op_curs = input("\nIngrese la opcion correspondiente: ")

        if int(op_curs) == 1:
            os.system("clear")
            curs_cod = input("Ingrese el codigo del curso: ")

            verif = Curso.getCursoDB(curs_cod)
            if verif is False:
                temp_curs = Curso()
                temp_curs.setCurso(curs_cod)
                temp_curs.insertCurso()
                print("\nCurso creado.")
                input("Presione una tecla para continuar...")
            else:
                print("\nEl codigo del curso ingresado ya existe.")
                input("Presione cualquier tecla para volver al menu.")

        elif int(op_curs) == 2:
            os.system("clear")
            lista_curso = Curso().getListaCurso()
            if len(lista_curso) != 0:
                for curso in lista_curso:
                    print("ID: " + str(curso.idCurso) + " - Codigo: " + curso.codigo)

                edit_op = input("\nIngrese el ID del curso que desea modificar: ")
                curso = Curso().getCursoDB(int(edit_op))

                new_codigo = input("Ingrese el nuevo codigo del curso: ")

                curso.setCurso(new_codigo)

                curso.actualizarCurso()
                print("\nCurso actualizado.")
                input("Presione cualquier tecla para continuar...")
            else:
                print("Curso no tiene datos cargados.")
                input("Presione cualquier tecla para continuar.")

        elif int(op_curs) == 3:
            lista_curso = Curso().getListaCurso()
            if len(lista_curso) != 0:
                for curso in lista_curso:
                    ver = curso.verificarCurso()
                    print("ID: " + str(curso.idCurso) +
                          " - Codigo: " + curso.codigo +
                          " - Cantidad Alumnos: " + str(ver[0]["cantidad"]))

                curs_id = input("Ingrese el ID del curso que desea eliminar: ")
                curso = Curso().getCursoDB(int(curs_id))
                ver_curso = curso.verificarCurso()

                if ver_curso[0]["cantidad"] == 0 and curso is not False:
                    curso.eliminarCurso()
                    print("\nCurso eliminado.")
                    input("Presione una tecla para continuar...")
                elif ver_curso[0]["cantidad"] > 0 and curso is not False:
                    print("\nNo se pudo eliminar debido a que tiene alumnos dentro.")
                    input("Presione una tecla para continuar...")
                else:
                    print("\nEl curso no existe.")
                    input("Presione una tecla para continuar...")
            else:
                print("Curso no tiene datos cargados.")
                input("Presione una tecla para continuar...")

        elif int(op_curs) == 4:
            os.system("clear")
            lista_curso = Curso().getListaCurso()
            for curso in lista_curso:
                ver = Curso.verificarCurso(curso)
                print("ID: " + str(curso.idCurso) +
                      " - Codigo: " + curso.codigo +
                      " - Cantidad Alumnos: " + str(ver[0]["cantidad"]))

            print("\nLista cargada exitosamente.")
            input("Presione cualquier boton para continuar...")

    elif int(opcion) == 2:
        os.system("clear")
        curso_data = DB().run("select * from Curso")
        curso_data_fetch = curso_data.fetchall()
        if curso_data_fetch.__len__() == 0:
            print("No hay datos insertados en Curso.")
            input("Presione cualquier tecla para volver al menu.")
        else:
            print("¿Que desea hacer con Profesor?: \n")
            print("1. Crear Profesor")
            print("2. Editar Profesor")
            print("3. Eliminar Profesor \n")

            op_prof = input("\nIngrese la opcion correspondiente: ")

            if int(op_prof) == 1:
                os.system("clear")
                nom = input("Ingrese el nombre del profesor: ")
                apell = input("Ingrese el apellido del profesor: ")
                fecha_nac = input("Ingrese la fecha de nacimiento del profesor (utilice '/'): ")

                prof = Profesor()

                prof.setNombre(nom)
                prof.setApellido(apell)

                fecha_nac_split = fecha_nac.split("/", 2)

                prof.setFechaNac(int(fecha_nac_split[2]), int(fecha_nac_split[1]), int(fecha_nac_split[0]))

                prof.insertProfesor()

                print("\nSe ha creado el profesor correctamente.")
                input("Presione cualquier tecla para continuar...")
            elif int(op_prof) == 2:
                os.system("clear")
                curs = DB().run("select * from Profesor")
                curs_fetch = curs.fetchall()
                if len(curs_fetch) == 0:
                    print("Profesor no tiene datos insertados.")
                    input("Presione cualquier boton para continuar...")
                else:
                    pass


    elif int(opcion) == 3:
        os.system("clear")
        curso_data = DB().run("select * from Curso")
        curso_data_fetch = curso_data.fetchall()
        if curso_data_fetch.__len__() == 0:
            print("No hay datos insertados en Curso.")
            input("Presione cualquier tecla para volver al menu.")
        else:
            print("¿Que desea hacer con Alumno?: \n")
            print("1. Crear Alumno")
            print("2. Editar Alumno")
            print("3. Eliminar Alumno")
            print("4. Mostrar Alumnos \n")
            op = input("\nIngrese la opcion correspondiente: ")

            if int(op) == 1:
                os.system("clear")
                nom = input("Ingrese el nombre del alumno: ")
                apell = input("Ingrese el apellido del alumno: ")
                fecha_nac = input("Ingrese la fecha de nacimiento del alumno (utilice '/'): ")
                fecha_nac_spliteada = fecha_nac.split("/", 2)
                curso_id = input("Ingrese el curso al que asiste el alumno: ")

                temp_alum = Alumno()

                temp_alum.setNombre(nom)
                temp_alum.setApellido(apell)
                temp_alum.setFechaNac(int(fecha_nac_spliteada[2]), int(fecha_nac_spliteada[1]), int(fecha_nac_spliteada[0]))

                verif2 = Curso().getCursoDB(curso_id)
                if verif2 is False:
                    while verif2 is False:
                        print("El curso ingresado no existe, vuelva a ingresar un curso valido.")
                        curso = input("Reingrese el curso: ")
                        verif2 = Curso().getCursoDB(curso)
                temp_alum.setCurso(verif2)

                temp_alum.insertAlumno()

            elif int(op) == 2:
                alumno_data = DB().run("select * from Alumno")
                alumno_data_fetch = alumno_data.fetchall()
                if alumno_data_fetch.__len__() == 0:
                    print("\nAlumno no tiene datos, inserte algun valor primero.")
                    input("Presione cualquier tecla para retornar al menu.")
                else:
                    os.system("clear")
                    lista_alumnos = Alumno.selectListaAlumnos()
                    for alumno in lista_alumnos:
                        print("ID: " + str(alumno.idPersona) +
                              " - Nombre: " + alumno.nombre +
                              " - Apellido: " + alumno.apellido +
                              " - Fecha de Nacimiento: " + str(alumno.fecha_nacimiento) +
                              " - Curso: " + alumno.curso.codigo)

                    print("\n¿Que ID desea modificar?")
                    alumno_id = input("Ingrese el ID: ")

                    alumno = Alumno.getAlumno(alumno_id)

                    if alumno is False:
                        print("\nEl alumno no existe.")
                        print("Presione una tecla para continuar...")
                        input()
                    else:
                        os.system("clear")
                        new_nom = input("Ingrese (si quiere) un nuevo nombre: ")
                        new_apell = input("Ingrese (si quiere) un nuevo apellido: ")
                        new_curso = input("Ingrese (si quiere) un nuevo curso: ")
                        new_fecha_nac = input("Ingrese (si quiere) una nueva fecha de nacimiento (Formato: DD/MM/AA): ")

                        new_fecha_nac_separada = new_fecha_nac.split("/", 2)

                        if new_nom is not '':
                            alumno.setNombre(new_nom)
                        if new_apell is not '':
                            alumno.setApellido(new_apell)
                        if new_fecha_nac is not '':
                            alumno.setFechaNac(int(new_fecha_nac_separada[2]), int(new_fecha_nac_separada[1]),
                                               int(new_fecha_nac_separada[0]))
                        if new_curso is not '':
                            alumno.setCurso(Curso.getCursoDB(new_curso))

                        alumno.actualizarAlumno()

                        print("\nAlumno actualizado.")
                        input("Presione cualquier tecla para continuar...")


            elif int(op) == 3:
                alumno_data = DB().run("select * from Alumno")
                alumno_data_fetch = alumno_data.fetchall()
                if alumno_data_fetch.__len__() == 0:
                    print("Alumno no tiene datos, inserte algun valor primero.")
                    input("Presione cualquier tecla para volver al menu.")

                else:
                    os.system("clear")
                    lista_alumnos = Alumno.selectListaAlumnos()
                    for alumno in lista_alumnos:
                        print("ID: " + str(alumno.idPersona) +
                              " - Nombre: " + alumno.nombre +
                              " - Apellido: " + alumno.apellido +
                              " - Fecha de Nacimiento: " + str(alumno.fecha_nacimiento) +
                              " - Curso: " + alumno.curso.codigo)

                    alum_id = input("\nIngrese el ID del alumno que desea eliminar: ")
                    alumno = Alumno().getAlumno(alum_id)
                    if alumno is False:
                        print("\nEl alumno no existe.")
                        input("Presione una tecla para continuar...")
                    else:
                        alumno.borrarAlumno()

                        print("\nAlumno borrado exitosamente.")
                        input("Presione cualquier tecla para continuar...")

            elif int(op) == 4:
                os.system("clear")
                lista_alumnos = Alumno.selectListaAlumnos()

                if lista_alumnos is False:
                    print("Alumno no tiene datos cargados.")
                    input("Presione una tecla para continuar...")
                else:
                    for alumno in lista_alumnos:
                        print("ID: " + str(alumno.idPersona) +
                              " - Nombre: " + alumno.nombre +
                              " - Apellido: " + alumno.apellido +
                              " - Fecha de Nacimiento: " + str(alumno.fecha_nacimiento) +
                              " - Curso: " + alumno.curso.codigo)
                    print("\nLista cargada exitosamente.")
                    input("Pulse una tecla para continuar...")

    elif int(opcion) == 4:
        pass