from db import DB


class Curso(object):
    idCurso = None
    codigo = None

    def setID(self, id):
        self.idCurso = id

    def setCurso(self, cod):
        self.codigo = cod

    @staticmethod
    def getCursoID(curs_cod):
        curso_data = DB().run("select idCurso from Curso where codigo = '" + curs_cod + "'")
        id_fetch = curso_data.fetchall()
        return id_fetch[0]["idCurso"]

    @staticmethod
    def getCursoDB(curs_codigo):
        if type(curs_codigo) is not int:
            curso_data = DB().run("select * from Curso where idCurso = " + str(Curso.getCursoID(curs_codigo)))
            curs_fetch = curso_data.fetchall()
        else:
            curso_data = DB().run("select * from Curso where idCurso = " + str(curs_codigo))
            curs_fetch = curso_data.fetchall()

        if len(curs_fetch) == 0:
            return False
        temp_curs = Curso()
        temp_curs.setID(curs_fetch[0]["idCurso"])
        temp_curs.setCurso(curs_fetch[0]["codigo"])
        return temp_curs


    def insertCurso(self):
        DB().run("insert into Curso values(%s, '%s')" % ("NULL", self.codigo))