from ej_5.class_artista import Artista
from ej_5.class_autor import Autor


class Cancion(object):
    titulo = None

    def __init__(self):
        self.lista_autores = []
        self.lista_artistas = []

    def setTitulo(self, titulo):
        self.titulo = titulo

    def agregarArtista(self, nombre, apellido, año, mes, dia):
        temp_art = Artista()

        temp_art.setNombre(nombre)
        temp_art.setApellido(apellido)
        temp_art.setFechaNac(año, mes, dia)

        self.lista_artistas.append(temp_art)

    def agregarAutor(self, nombre, apellido, año, mes, dia, nacionalidad):
        temp_aut = Autor()

        temp_aut.setNombre(nombre)
        temp_aut.setApellido(apellido)
        temp_aut.setFechaNac(año, mes, dia)
        temp_aut.setNacionalidad(nacionalidad)

        self.lista_autores.append(temp_aut)

