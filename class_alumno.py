from class_persona import Persona
from db import DB
from class_curso import Curso


class Alumno(Persona):
    curso = None

    def setCurso(self, curso):
        self.curso = curso

    def insertAlumno(self):
        DB().run("insert into Alumno values(NULL, '%s', '%s', '%s', %i)"
                 % (self.nombre, self.apellido, str(self.fecha_nacimiento), self.curso.idCurso))

    def actualizarAlumno(self, nom, apell, ):
        DB().run

    @staticmethod
    def selectListaAlumnos():
        students_dictionary = DB().run("select * from Alumno")
        return students_dictionary

    @staticmethod
    def getAlumno(nom, apell):
        students_dictionary = Alumno.selectListaAlumnos()
        for student in students_dictionary:
            if student["nombre"] == nom and student["apellido"] == apell:
                temp_alum = Alumno()
                temp_alum.setID(student["idAlumno"])
                temp_alum.setNombre(student["nombre"])
                temp_alum.setApellido(student["apellido"])
                temp_alum.setCurso(Curso().getCursoDB(student["Curso_idCurso"]))

                #fecha_spliteada = str(student)

                temp_alum.fecha_nacimiento = student["fecha_nacimiento"]

        return temp_alum