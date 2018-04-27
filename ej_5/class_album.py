import datetime


class Album(object):
    titulo = None

    def __init__(self):
        self.lista_canciones = []

    def añadirCancion(self, temp_canc):
        self.lista_canciones.append(temp_canc)

    def devolverArtistas(self):
        temp_lista_artistas = []

        for cancion in self.lista_canciones:
            for artista in cancion.lista_artistas:
                if not artista in temp_lista_artistas:
                    temp_lista_artistas.append(artista)

        return temp_lista_artistas

    def devolverArtistaInfluy(self):
        cant_apariciones = 0
        old_cant_apariciones = 0
        art_influyente = None

        temp_lista_artistas = self.devolverArtistas()
        for art in temp_lista_artistas:
            for cancion in self.lista_canciones:
                for art_2 in cancion.lista_artistas:
                    if art == art_2:
                        cant_apariciones += 1
            if cant_apariciones > old_cant_apariciones:
                art_influyente = art
                old_cant_apariciones = cant_apariciones

        return art_influyente

