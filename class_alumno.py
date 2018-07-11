from class_persona import Persona
from db import DB


class Alumno(Persona):
    curso = None

    def setCurso(self, curso):
        self.curso = curso

    def insertAlumno(self):
        DB().run("insert into Alumno values(NULL, '%s', '%s', '%s', %i)"
                 % (self.nombre, self.apellido, str(self.fecha_nacimiento), self.curso.idCurso))