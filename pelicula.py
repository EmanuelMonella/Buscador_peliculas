from actor import Actor

class Pelicula:
    def __init__(self, titulo, actores, sinopsis, puntuacion, poster):
        self.__titulo = titulo
        self.__actores = [Actor(actor) for actor in actores]
        self.__sinopsis = sinopsis
        self.__puntuacion = puntuacion
        self.__poster = poster

    @classmethod
    def cargar_pelicula_desde_json(cls, json):
        return cls(
            titulo=json['titulo'],
            actores=json['actores'],
            sinopsis=json['sinopsis'],
            puntuacion=json['puntuacion'],
            poster=json['poster']
        )

    def __str__(self):
        return (f"Título: {self.__titulo}\n"
                f"Actores: {', '.join(str(actor) for actor in self.__actores)}\n"
                f"Sinopsis: {self.__sinopsis}\n"
                f"Puntuación: {self.__puntuacion}")

    def obtener_atributos(self):
        return {
            "titulo": self.__titulo,
            "actores": [actor.obtener_nombre() for actor in self.__actores],
            "sinopsis": self.__sinopsis,
            "puntuacion": self.__puntuacion,
            "poster": self.__poster,
        }
