class Actor:
    def __init__(self, nombre, pelicula=None):
        self.__nombre = nombre
        self.__pelicula = pelicula if pelicula else []

    def __agregar_pelicula_al_actor(self, pelicula):
        self.__pelicula.append(pelicula)

