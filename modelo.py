class Pelicula:
    def __init__(self, titulo, actores, sinopsis, puntuacion, poster):
        self.titulo = titulo
        self.actores = actores
        self.sinopsis = sinopsis
        self.puntuacion = puntuacion
        self.poster = poster

    def cargar_pelicula_desde_json(data):
        return Pelicula(
            titulo=data['titulo'],
            actores=data['actores'],
            sinopsis=data['sinopsis'],
            puntuacion=data['puntuacion'],
            poster=data['poster']
        )
