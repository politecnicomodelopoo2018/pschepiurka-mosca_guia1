from class_persona import Persona
from db import DB


class Profesor(Persona):
    def insertProfesor(self):
        DB().run("insert into Profesor values(NULL, '" +
                 self.nombre + "', '" +
                 self.apellido + "', '" +
                 str(self.fecha_nacimiento) + "')")

    def actualizarProfesor(self):
        DB().run("update Profesor set nombre = '" + self.nombre +
               "', apellido = '" + self.apellido +
               "', fecha_nacimiento = '" + str(self.fecha_nacimiento) +
               "' where idProfesor = " + str(self.idPersona))

    def eliminarProfesor(self):
        DB().run("delete from Profesor where idProfesor = " + str(self.idPersona))

    @staticmethod
    def getListaProfesor():
        temp_teacher_list = []
        teacher_dictionary = DB().run("select * from Profesor")
        for teacher in teacher_dictionary:
            temp_teach = Profesor()
            temp_teach.setID(teacher["idProfesor"])
            temp_teach.setNombre(teacher["nombre"])
            temp_teach.setApellido(teacher["apellido"])

            fecha_nac = str(teacher["fecha_nacimiento"]).split("-", 2)
            temp_teach.setFechaNac(int(fecha_nac[0]), int(fecha_nac[1]), int(fecha_nac[2]))

            temp_teacher_list.append(temp_teach)

        return temp_teacher_list

    @staticmethod
    def getProfesor(id_profesor):
        teach_dict = DB().run("select * from Profesor where idProfesor = " + id_profesor)
        teach_fetch = teach_dict.fetchall()

        if len(teach_fetch) == 0:
            return False
        else:
            temp_teach = Profesor()
            temp_teach.setID(teach_fetch[0]["idProfesor"])
            temp_teach.setNombre(teach_fetch[0]["nombre"])
            temp_teach.setApellido(teach_fetch[0]["apellido"])

            fecha_nac = str(teach_fetch[0]["fecha_nacimiento"]).split("-", 2)
            temp_teach.setFechaNac(int(fecha_nac[0]), int(fecha_nac[1]), int(fecha_nac[2]))

        return temp_teach

    def getMaterias(self):
        DB().run("select idMateria from Materia"
                 "where idProfesor = " + self.idPersona)