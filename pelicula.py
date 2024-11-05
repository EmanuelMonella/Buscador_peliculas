class Pelicula:
    def __init__(self, titulo, actores, sinopsis, puntuacion, poster):
        self.titulo = titulo
        self.actores = actores
        self.sinopsis = sinopsis
        self.puntuacion = puntuacion
        self.poster = poster

    @classmethod
    def cargar_pelicula_desde_json(cls, json):
        return cls(
            titulo=json['titulo'],
            actores=json['actores'],
            sinopsis=json['sinopsis'],
            puntuacion=json['puntuacion'],
            poster=json['poster']
        )