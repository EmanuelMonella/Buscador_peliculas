import json
from modelos.pelicula import Pelicula

class Catalogo:
    def __init__(self):
        self.__catalogo = self.cargar_catalogo()

    def cargar_catalogo(self):
        try:
            with open('peliculas/catalogo.json', 'r') as file:
                archivo = json.load(file)
                return [Pelicula.cargar_pelicula_desde_json(pelis) for pelis in archivo]
        except FileNotFoundError:
            print("Error: El archivo catalogo.json no se encontró.")
            return []
        except json.JSONDecodeError:
            print("Error: El archivo catalogo.json no es un JSON válido.")
            return []

    def gestionar_catalogo(self):
        return self.__catalogo

    def buscar_pelicula(self, nombre):
        return [
            pelicula for pelicula in self.__catalogo
            if nombre.lower() in pelicula.obtener_atributos()["titulo"].lower()]

    def buscar_actor(self, actores_input):
        actores = [actor.strip().lower() for actor in actores_input.split(',')]
        peliculas_encontradas = []
        for actor_nombre in actores:
            for pelicula in self.__catalogo:
                if pelicula.buscar_actor(actor_nombre):
                    peliculas_encontradas.append(pelicula)
        return list(set(peliculas_encontradas))

    def obtener_info_pelicula(self, titulo):
        for pelicula in self.__catalogo:
            if pelicula.obtener_atributos()["titulo"].strip().lower() == titulo.strip().lower():
                return pelicula
        return None
