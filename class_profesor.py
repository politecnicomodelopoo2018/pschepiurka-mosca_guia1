from class_persona import Persona
from db import DB


class Profesor(Persona):
    def insertProfesor(self):
        DB().run("insert into Profesor values(NULL, '" +
                 self.nombre + "', '" +
                 self.apellido + "', '" +
                 str(self.fecha_nacimiento) + "')")

    @staticmethod
    def getListaProfesor():
        temp_teacher_list = []
        teacher_dictionary = DB().run("select * from Profesor")
        teacher_dictionary

    def getMaterias(self):
        DB().run("select idMateria from Materia"
                 "where idProfesor = " + self.idPersona)