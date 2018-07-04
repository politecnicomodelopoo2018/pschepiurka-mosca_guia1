import json
from person_class import Person
import datetime

f = open("datos.json", "r")

d = json.loads(f.read())

person_list = []

for person in d["Personas"]:
    temp_pers = Person()

    if person["tipo"] == "Pasajero":
        temp_pers.type = person["tipo"]

        temp_pers.name = person["nombre"]
        temp_pers.lastname = person["apellido"]

        birthdate = str.split(person["fechaNacimiento"], "-", 2)

        temp_pers.birth_date = datetime.date(int(birthdate[0]), int(birthdate[1]), int(birthdate[2]))
        temp_pers.dni = person["dni"]
        if person["vip"] == 1:
            temp_pers.vip = "Premium"
        else:
            temp_pers.vip = "No tiene"

        if "solicitudesEspeciales" in person:
            temp_pers.special_requirements = person["solicitudesEspeciales"]
        else:
            temp_pers.special_requirements = "No tiene"

        person_list.append(temp_pers)

for person in person_list:
    print(person.type, "\n", person.name, "\n", person.lastname, "\n", person.birth_date, "\n", person.dni,
          "\n", person.vip, "\n", person.special_requirements)
    for i in range(2):
        print("\n")