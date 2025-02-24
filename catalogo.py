import json
from pelicula import Pelicula


class Catalogo:
    def __init__(self):
        self.__catalogo = self.cargar_catalogo()

    def cargar_catalogo(self):
        with open('peliculas/catalogo.json', 'r') as file:
            archivo = json.load(file)
            return [Pelicula.cargar_pelicula_desde_json(pelis) for pelis in archivo]

    def gestionar_catalogo(self):
        return self.__catalogo

    def buscar_pelicula(self, nombre):
        return [
            pelicula for pelicula in self.__catalogo
            if nombre.lower() in pelicula.obtener_atributos()["titulo"].lower()
        ]

    def buscar_actor(self, actores_input):
        actores = [actor.strip().lower() for actor in actores_input.split(',')]
        return [
            pelicula for pelicula in self.__catalogo
            if all(
                any(actor in a.lower() for a in pelicula.obtener_atributos()["actores"])
                for actor in actores
            )
        ]

    def obtener_info_pelicula(self, titulo):
        for pelicula in self.__catalogo:
            if pelicula.obtener_atributos()["titulo"].strip().lower() == titulo.strip().lower():
                return pelicula
        return None
