import json
from pelicula import Pelicula


class Catalogo:
    def __init__(self):
        self.catalogo = self.cargar_catalogo()

    def cargar_catalogo(self):
        with open('peliculas/catalogo.json', 'r') as file:
            data = json.load(file)
            return [Pelicula.cargar_pelicula_desde_json(p) for p in data]

    def buscar_pelicula(self, nombre):
        """
        Busca películas cuyo título contenga la cadena proporcionada.
        """
        return [pelicula for pelicula in self.catalogo if nombre.lower() in pelicula.titulo.lower()]

    def buscar_actor(self, actores_input):
        """
        Busca películas en las que participen todos los actores dados.
        """
        actores = [actor.strip().lower() for actor in actores_input.split(',')]
        return [pelicula for pelicula in self.catalogo if
                all(any(actor in a.lower() for a in pelicula.actores) for actor in actores)]

    def obtener_info_pelicula(self, titulo):
        """
        Devuelve la información de una película cuyo título coincida exactamente.
        """
        for pelicula in self.catalogo:
            if pelicula.titulo.strip().lower() == titulo.strip().lower():  # Ignora mayúsculas/minúsculas y espacios
                return pelicula
        return None

