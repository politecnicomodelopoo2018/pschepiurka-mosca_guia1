from ej_2_repaso.class_comida import Comida
from ej_2_repaso.class_familia import Familia
import datetime

lopez = Familia()

lopez.apellido = "Lopez"

lopez.ingresarMiembro("Nicolas", datetime.date(2001, 5, 16))
lopez.ingresarMiembro("Hugo", datetime.date(1959, 8 , 18))
lopez.ingresarMiembro("Maria", datetime.date(1984, 5, 4))

comida = Comida()
lista_comidas = []

comida.crearComida("hamburguesa", 295)
lista_comidas.append(comida)

comida2 = Comida()
comida2.crearComida("salchicha", 301)
lista_comidas.append(comida2)

comida3 = Comida()
comida3.crearComida("ensalada", 152)
lista_comidas.append(comida3)

lopez.miembros[0].personaComer(lista_comidas[1])
lopez.miembros[0].personaComer(lista_comidas[1])
lopez.miembros[0].personaComer(lista_comidas[2])

lopez.miembros[1].personaComer(lista_comidas[0])
lopez.miembros[1].personaComer(lista_comidas[1])
lopez.miembros[1].personaComer(lista_comidas[1])

lopez.miembros[2].personaComer(lista_comidas[2])
lopez.miembros[2].personaComer(lista_comidas[2])
lopez.miembros[2].personaComer(lista_comidas[1])

print(lopez.getPromCaloriasPers("Nicolas"))
print(lopez.getPromCaloriasPers("Hugo"))
print(lopez.getPromCaloriasPers("Maria"))

print("\n")
print(lopez.promTotalFam())
print(lopez.menCaloriasFam())
print(lopez.mayCaloriasFam())

