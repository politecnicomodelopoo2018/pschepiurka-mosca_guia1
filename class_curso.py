from db import DB


class Curso(object):
    idCurso = None
    codigo = None

    def setID(self, id):
        self.idCurso = id

    def setCurso(self, cod):
        self.codigo = cod

    @staticmethod
    def getCursoDB(curs_codigo):
        curso_data = DB().run("select * from Curso where idCurso = " + str(curs_codigo))
        d = curso_data.fetchall()
        if len(d) == 0:
            return False
        temp_curs = Curso()
        temp_curs.setID(d["idCurso"])
        temp_curs.setCurso(d["codigo"])
        return temp_curs


    def insertCurso(self):
        DB().run("insert into Curso values(%s, '%s')" % ("NULL", self.codigo))