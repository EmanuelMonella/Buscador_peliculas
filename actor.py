class Actor:
    def __init__(self, nombre):
        self.__nombre = nombre

    def __str__(self):
        return self.__nombre

    def obtener_nombre(self):
        return self.__nombre
