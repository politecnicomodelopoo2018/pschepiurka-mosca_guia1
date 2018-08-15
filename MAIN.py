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

                if curso is not False:
                    new_codigo = input("Ingrese el nuevo codigo del curso: ")

                    if curso.codigo == new_codigo:
                        print("El codigo ingresado es el mismo.")
                        input("Presione cualquier tecla para continuar...")
                    else:
                        if new_codigo is not '':
                            curso.setCurso(new_codigo)

                        curso.actualizarCurso()
                        print("\nCurso actualizado.")
                        input("Presione cualquier tecla para continuar...")
                else:
                    print("\nEl ID ingresado no existe.")
                    input("Presione cualquier tecla para continuar...")
            else:
                print("Curso no tiene datos cargados.")
                input("Presione cualquier tecla para continuar.")

        elif int(op_curs) == 3:
            os.system("clear")
            lista_curso = Curso().getListaCurso()
            if len(lista_curso) != 0:
                for curso in lista_curso:
                    ver = curso.verificarCurso()
                    print("ID: " + str(curso.idCurso) +
                          " - Codigo: " + curso.codigo +
                          " - Cantidad Alumnos: " + str(ver[0]["cantidad"]))

                curs_id = input("\nIngrese el ID del curso que desea eliminar: ")
                curso = Curso().getCursoDB(int(curs_id))

                if curso is False:
                    print("\nEl ID ingresado no existe.")
                    input("Presione cualquier tecla para continuar...")
                else:
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
            print("3. Eliminar Profesor")
            print("4. Mostrar Profesores \n")

            op_prof = input("\nIngrese la opcion correspondiente: ")

            if int(op_prof) == 1:
                os.system("clear")
                nom = input("Ingrese el nombre del profesor: ")
                apell = input("Ingrese el apellido del profesor: ")
                fecha_nac = input("Ingrese la fecha de nacimiento del profesor (utilice '/'): ")

                nombre_completo = nom + " " + apell
                verif = Profesor().getProfesor(nombre_completo)

                if verif is False:
                    prof = Profesor()

                    prof.setNombre(nom)
                    prof.setApellido(apell)

                    fecha_nac_split = fecha_nac.split("/", 2)

                    prof.setFechaNac(int(fecha_nac_split[2]), int(fecha_nac_split[1]), int(fecha_nac_split[0]))

                    prof.insertProfesor()

                    print("\nSe ha creado el profesor correctamente.")
                    input("Presione cualquier tecla para continuar...")
                else:
                    print("El profesor ya existe.")
                    input("Presione cualquier tecla para continuar...")

            elif int(op_prof) == 2:
                os.system("clear")
                prof_list = Profesor().getListaProfesor()
                if len(prof_list) == 0:
                    print("Profesor no tiene datos insertados.")
                    input("Presione cualquier boton para continuar...")
                else:
                    for profesor in prof_list:
                        print("ID: " + str(profesor.idPersona) +
                              " - Nombre: " + profesor.nombre +
                              " - Apellido: " + profesor.apellido +
                              " - Fecha de Nacimiento: " + str(profesor.fecha_nacimiento))

                    modif_op = input("\nIngrese el ID del profesor que desea modificar: ")
                    profesor = Profesor().getProfesor(int(modif_op))

                    if profesor is False:
                        print("\nEl ID ingresado no existe.")
                        input("Presione cualquier tecla para continuar...")
                    else:
                        new_nom = input("Ingrese (si quiere) un nuevo nombre: ")
                        new_apell = input("Ingrese (si quiere) un nuevo apellido: ")
                        new_fecha_nac = input("Ingrese (si quiere) una nueva fecha de nacimiento (Formato DD/MM/AA): ")

                        new_fecha_nac_separada = new_fecha_nac.split("/", 2)

                        if new_nom is not '':
                            profesor.setNombre(new_nom)
                        if new_apell is not '':
                            profesor.setApellido(new_apell)
                        if new_fecha_nac is not '':
                            profesor.setFechaNac(int(new_fecha_nac_separada[2]), int(new_fecha_nac_separada[1]),
                                               int(new_fecha_nac_separada[0]))

                        profesor.actualizarProfesor()
                        print("\nProfesor actualizado exitosamente.")
                        input("Presione cualquier tecla para continuar...")

            elif int(op_prof) == 3:
                os.system("clear")
                prof_list = Profesor().getListaProfesor()
                if len(prof_list) == 0:
                    print("Profesor no tiene datos insertados.")
                    input("Presione cualquier boton para continuar...")
                else:
                    for profesor in prof_list:
                        cant_materias = profesor.verificarProfesor()
                        print("ID: " + str(profesor.idPersona) +
                              " - Nombre: " + profesor.nombre +
                              " - Apellido: " + profesor.apellido +
                              " - Fecha de Nacimiento: " + str(profesor.fecha_nacimiento) +
                              " - Cantidad de Materias: " + str(cant_materias[0]["cantidad_materias"]))

                    elim_op = input("\nIngrese el ID del profesor que desea eliminar: ")
                    profesor = Profesor().getProfesor(int(elim_op))
                    ver_prof = profesor.verificarProfesor()

                    if profesor is False:
                        print("\nEl ID ingresado no existe.")
                        input("Presione cualquier tecla para continuar...")
                    elif ver_prof[0]["cantidad_materias"] > 0:
                        print("\nEl profesor no puede ser eliminado porque tiene materias asociadas a el.")
                        input("Presione cualquier tecla para continuar...")
                    else:
                        profesor.eliminarProfesor()
                        print("\nProfesor eliminado exitosamente.")
                        input("Presione cualquier tecla para continuar...")

            elif int(op_prof) == 4:
                os.system("clear")
                prof_list = Profesor().getListaProfesor()
                if len(prof_list) == 0:
                    print("Profesor no tiene datos insertados.")
                    input("Presione cualquier boton para continuar...")
                for profesor in prof_list:
                    print("ID: " + str(profesor.idPersona) +
                          " - Nombre: " + profesor.nombre +
                          " - Apellido: " + profesor.apellido +
                          " - Fecha de Nacimiento: " + str(profesor.fecha_nacimiento))

                print("\nLista cargada exitosamente.")
                input("Presione cualquier tecla para continuar...")

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

                nombre_completo = (nom + " " + apell)
                verif = Alumno().getAlumno(nombre_completo)

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
                lista_alumnos = Alumno.selectListaAlumnos()
                if len(lista_alumnos) == 0:
                    print("\nAlumno no tiene datos, inserte algun valor primero.")
                    input("Presione cualquier tecla para retornar al menu.")
                else:
                    os.system("clear")
                    for alumno in lista_alumnos:
                        print("ID: " + str(alumno.idPersona) +
                              " - Nombre: " + alumno.nombre +
                              " - Apellido: " + alumno.apellido +
                              " - Fecha de Nacimiento: " + str(alumno.fecha_nacimiento) +
                              " - Curso: " + alumno.curso.codigo)

                    print("\n¿Que ID desea modificar?")
                    alumno_id = input("Ingrese el ID: ")

                    alumno = Alumno.getAlumno(int(alumno_id))

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
                lista_alumnos = Alumno.selectListaAlumnos()
                if len(lista_alumnos) == 0:
                    print("Alumno no tiene datos, inserte algun valor primero.")
                    input("Presione cualquier tecla para volver al menu.")
                else:
                    os.system("clear")
                    for alumno in lista_alumnos:
                        print("ID: " + str(alumno.idPersona) +
                              " - Nombre: " + alumno.nombre +
                              " - Apellido: " + alumno.apellido +
                              " - Fecha de Nacimiento: " + str(alumno.fecha_nacimiento) +
                              " - Curso: " + alumno.curso.codigo)

                    alum_id = input("\nIngrese el ID del alumno que desea eliminar: ")
                    alumno = Alumno().getAlumno(int(alum_id))
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
        lista_profesor = Profesor().getListaProfesor()
        lista_curso = Curso().getListaCurso()

        if len(lista_curso) == 0 and len(lista_profesor) == 0:
            print("Profesor y Curso no tienen datos registrados.")
            input("Presione cualquier tecla para continuar...")
        elif len(lista_curso) == 0:
            print("Curso no tiene datos registrados.")
            input("Presione cualquier tecla para continuar...")
        elif len(lista_profesor) == 0:
            print("Profesor no tiene datos registrados.")
            input("Presione cualquier tecla para continuar...")
        else:
            os.system("clear")
            print("¿Que desea hacer con Materia?: \n")
            print("1. Crear Materia")
            print("2. Modificar Materia")
            print("3. Eliminar Materia")
            print("4. Mostrar Materia \n")
            op_mat = input("Ingrese la opcion correspondiente: ")

            if int(op_mat) == 1:
                os.system("clear")
                nom = input("Ingrese el nombre de la materia: ")
                prof = input("Ingrese el profesor que da la materia: ")
                curs = input("Ingrese el curso en el que se da la materia: ")

                verif = Profesor().getProfesor(prof)
                verif2 = Curso().getCursoDB(curs)

                if verif is False and verif2 is False:
                    print("\nNi el profesor ni el curso existen.")
                    input("Presione cualquier tecla para continuar...")
                elif verif is False:
                    print("\nEl profesor no existe.")
                    input("Presione cualquier tecla para continuar...")
                elif verif2 is False:
                    print("\nEl curso no existe.")
                    input("Presione cualquier tecla para continuar...")
                else:
                    temp_mat = Materia()
                    temp_mat.setNombre(nom)
                    temp_mat.setProfesor(Profesor().getProfesor(prof))
                    temp_mat.setCurso(Curso().getCursoDB(curs))

                    temp_mat.insertarMateria()

                    print("\nMateria creada correctamente.")
                    input("Presione cualquier tecla para continuar...")

            if int(op_mat) == 2:
                os.system("clear")
                lista_materias = Materia().selectListaMaterias()
                if len(lista_materias) == 0:
                    print("Materia no tiene datos registrados.")
                    input("Presione cualquier tecla para continuar...")
                else:
                    for materia in lista_materias:
                        print("ID: " + str(materia.idMateria) +
                              " - Nombre: " + materia.nombre +
                              " - Profesor: " + materia.profesor.nombre + " " + materia.profesor.apellido +
                              " - Curso: " + materia.curso.codigo)
                    mod_op = input("\nIngrese el ID de la materia que desea modificar: ")
                    temp_mat = Materia().selectMateria(mod_op)

                    if temp_mat is False:
                        print("\nEl ID ingresado no existe.")
                        input("Presione cualquier tecla para continuar...")
                    else:
                        new_name = input("Ingrese (si quiere) un nuevo nombre: ")
                        new_prof = input("Ingrese (si quiere) un nuevo profesor: ")
                        new_curs = input("Ingrese (si quiere) un nuevo curso: ")

                        verif = Profesor().getProfesor(new_prof)
                        verif2 = Curso().getCursoDB(new_curs)

                        if verif is False and verif2 is False:
                            print("Ni el profesor ni el curso existen.")
                            input("Presione cualquier tecla para continuar...")
                        elif verif is False:
                            print("El profesor no existe.")
                            input("Presione cualquier tecla para continuar...")
                        elif verif2 is False:
                            print("El curso no existe.")
                            input("Presione cualquier tecla para continuar...")
                        else:
                            if new_name is not '':
                                temp_mat.setNombre(new_name)
                            if new_prof is not '':
                                temp_mat.setProfesor(Profesor().getProfesor(new_prof))
                            if new_curs is not '':
                                temp_mat.setCurso(Curso().getCursoDB(new_curs))

                            temp_mat.actualizarMateria()

                            print("\nMateria actualizada correctamente.")
                            input("Presione cualquier tecla para continuar...")

            if int(op_mat) == 3:
                os.system("clear")
                lista_materias = Materia().selectListaMaterias()
                if len(lista_materias) == 0:
                    print("Materia no tiene datos registrados.")
                    input("Presione cualquier tecla para continuar...")
                else:
                    for materia in lista_materias:
                        print("ID: " + str(materia.idMateria) +
                              " - Nombre: " + materia.nombre +
                              " - Profesor: " + materia.profesor.nombre + " " + materia.profesor.apellido +
                              " - Curso: " + materia.curso.codigo)
                    mod_op = input("\nIngrese el ID de la materia que desea eliminar: ")
                    temp_mat = Materia().selectMateria(mod_op)

                    if temp_mat is False:
                        print("El ID ingresado no existe.")
                        input("Presione cualquier tecla para continuar...")
                    else:
                        temp_mat.borrarMateria()

                        print("Materia borrada correctamente.")
                        input("Presione cualquier tecla para continuar...")

            elif int(op_mat) == 4:
                os.system("clear")
                lista_materias = Materia().selectListaMaterias()
                if len(lista_materias) == 0:
                    print("Materia no tiene datos registrados.")
                    input("Presione cualquier tecla para continuar...")
                else:
                    for materia in lista_materias:
                        print("ID: " + str(materia.idMateria) +
                              " - Nombre: " + materia.nombre +
                              " - Profesor: " + materia.profesor.nombre + " " + materia.profesor.apellido +
                              " - Curso: " + materia.curso.codigo)

                    print("\nDatos cargados correctamente.")
                    input("Presione cualquier tecla para continuar...")