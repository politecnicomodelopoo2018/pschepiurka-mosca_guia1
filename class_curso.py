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
        curso_data = DB().run("select * from Curso")
        for line in curso_data:
            if line["codigo"] == curs_codigo:
                temp_curs = Curso()
                temp_curs.setID(line["idCurso"])
                temp_curs.setCurso(line["codigo"])
                return temp_curs
        return False

    def insertCurso(self):
        DB().run("insert into Curso values(%s, '%s')" % ("NULL", self.codigo))