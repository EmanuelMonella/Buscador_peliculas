from ui.catalogo import Catalogo
from PySide6.QtWidgets import QMessageBox

class Controlador:
    def __init__(self):
        self.catalogo = Catalogo()

    def buscar_pelicula(self, nombre_pelicula):
        return self.catalogo.buscar_pelicula(nombre_pelicula)

    def manejar_busqueda(self, nombre_pelicula, lista_resultados):
        lista_resultados.clear()
        if nombre_pelicula:
            coincidencias = self.buscar_pelicula(nombre_pelicula)
            if coincidencias:
                for pelicula in coincidencias:
                    lista_resultados.addItem(pelicula.titulo)
            else:
                return "No se encontraron coincidencias."
        else:
            return "Por favor, ingrese un nombre de película."

    def mostrar_info_pelicula(self, item):
        if item:
            pelicula = item.data(1)
            if pelicula:
                return pelicula
        return None