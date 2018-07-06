from class_persona import Persona
from db import DB


class Profesor(Persona):
    def insertProfesor(self):
        DB().run("insert into Profesor values(NULL, %s, %s, %s, %i)"
                 % (self.nombre, self.apellido, str(self.fecha_nacimiento)))

    def getMaterias(self):
        DB().run("select idMateria from Materia"
                 "where idProfesor = " + self.idPersona)