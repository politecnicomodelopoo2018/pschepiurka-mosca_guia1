import pymysql


class DB(object):
    __instance = None
    __HOST = None
    __USER = None
    __PASSWD = None
    __DB = None

    def __new__(cls, *args, **kwargs):
        if DB.__instance is None:
            DB.__instance = object.__new__(cls)
        return DB.__instance

    def setConexion(self, host, user, passwd, db):
        self.__HOST = host
        self.__USER = user
        self.__PASSWD = passwd
        self.__DB = db

    def run(self, query):
        db = pymysql.connect(host=self.__HOST,
                             user=self.__USER,
                             passwd=self.__PASSWD,
                             db=self.__DB,
                             charset="utf8",
                             autocommit=True)

        cursor = db.cursor(pymysql.cursors.DictCursor)

        cursor.execute(query)
        cursor_fetcheado = cursor.fetchall()
        db.close()

        return cursor_fetcheado