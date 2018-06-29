import datetime
import json


class Persona(object):
    __nombre = None
    __apellido = None
    __fecha_nac = None

    def setNombre(self, nom):
        self.__nombre = nom

    def setApellido(self, apell):
        self.__apellido = apell

    def setFechaNac(self, año, mes, dia):
        self.__fecha_nac = datetime.date(año, mes, dia)

    def serializar(self):
        d = {
            "nombre": self.__nombre,
            "apellido": self.__apellido,
            "fecha_Nac": str(self.__fecha_nac) # Para que el JSON no crashee, variables que no sean tipo str, float o int se transforman
        }
        return d

    def deserializar(self, d):
        self.__nombre = d["nombre"]
        self.__apellido = d["apellido"]
        self.__fecha_nac = datetime.date.strptime(d["fecha_Nac"])

#       Main       #

#Proceso de pasar clases a JSON

#Declaracion de lista_personas y apertura del archivo .json
lista_personas = []
f = open("listaPersonas.json", "w")

#Creacion de personas y agregacion de estas en la lista_personas
op = input("Cuantas personas desea crear? \n")
for persona in range(int(op)):
    temp_pers = Persona()

    n = input("Ingrese el nombre: ")
    a = input("Ingrese el apellido: ")
    fn = input("Ingrese la fecha de nacimiento: ")

    fn_split = str.split(fn, "/", 2)

    temp_pers.setNombre(n)
    temp_pers.setApellido(a)
    temp_pers.setFechaNac(int(fn_split[2]), int(fn_split[1]), int(fn_split[0]))

    lista_personas.append(temp_pers)
    print("\n Persona añadida exitosamente! \n")

#Creacion del Diccionario
d = {"personas": []}

#Meter la lista_personas en la lista "personas" dentro de diccionario
for p in lista_personas:
    d["personas"].append(p.serializar())

#Pasar de Diccionario a JSON y agregarlo al archivo y cierre del mismo
#Diferencia entre DUMPS y DUMP: El DUMP lo escribe en binario, el DUMPS en str
#El ensure_ascii=False es para que escriba valores que no estan dentro de la tabla ASCII, como las "Ñ"
#El indent=4 es para que se vea lindo dentro del archivo
f.write(json.dumps(d, ensure_ascii=False, indent=4))
f.close()

#Proceso de recuperacion de datos del archivo .json

#Apertura del archivo, Parseo de JSON al Diccionario y creacion de la nueva lista donde se almacenan las personas
f = open("listaPersonas.json", "r")
d = json.loads(f.read())
new_lista_personas = []

#Creacion de las personas con los datos recuperados del archivo .json
for item in d["personas"]:
    temp_pers = Persona()
    temp_pers.deserializar(item)
    new_lista_personas.append(temp_pers)

#Cierre del archivo anteriormente abierto
f.close()