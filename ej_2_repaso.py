from class_comida import Comida
from class_familia import Familia
import datetime

lopez = Familia()

lopez.apellido = "Lopez"

lopez.ingresarMiembro("Nicolás", datetime.date(2001, 5, 16))
lopez.ingresarMiembro("Hugo", datetime.date(1959, 8 , 18))
lopez.ingresarMiembro("Maria", datetime.date(1984, 5, 4))

comida = Comida()
lista_comidas = []

comida.crearComida("hamburguesa", 295)
lista_comidas.append(comida)

comida2 = Comida()
comida.crearComida("salchicha", 301)
lista_comidas.append(comida2)

comida3 = Comida()
comida.crearComida("ensalada", 152)
lista_comidas.append(comida3)

lopez.personaComer("Hugo")

