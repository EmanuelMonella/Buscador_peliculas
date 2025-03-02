from modelos.actor import Actor

class Pelicula:
    def __init__(self, titulo, actores, sinopsis, puntuacion, poster):
        self.__titulo = titulo
        self.__actores = [Actor(actor) for actor in actores]
        self.__sinopsis = sinopsis
        self.__puntuacion = puntuacion
        self.__poster = poster

    @classmethod
    def cargar_pelicula_desde_json(cls, archivo_json):
        return cls(
            titulo=archivo_json['titulo'],
            actores=archivo_json['actores'],
            sinopsis=archivo_json['sinopsis'],
            puntuacion=archivo_json['puntuacion'],
            poster=archivo_json['poster']
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

    def buscar_actor(self, actor_nombre):
        return any(actor_nombre.lower() in actor.obtener_nombre().lower() for actor in self.__actores)
