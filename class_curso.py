from db import DB


class Curso(object):
    idCurso = None
    codigo = None

    def setCurso(self, id, cod):
        self.idCurso = id
        self.codigo = cod

    def insertCurso(self):
        DB().run("insert into Curso values(%i, %s)"
                 % (self.idCurso, self.codigo))