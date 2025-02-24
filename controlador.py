from PySide6.QtCore import Slot
from PySide6.QtWidgets import QMessageBox
from catalogo import Catalogo
from ui.ventana_busqueda import BuscadorPeliculas
from ui.ventana_actor import VentanaBuscarPorActor
from ui.ventana_info import VentanaInfo


class Controlador:
    def __init__(self):
        self.__catalogo = Catalogo()
        self.__buscador = BuscadorPeliculas()
        self.__ventana_actor = None
        self.__ventana_info = None

        self.__buscador.buscar_pelicula.connect(self.buscar_pelicula)
        self.__buscador.mostrar_info_pelicula.connect(self.mostrar_info_pelicula)
        self.__buscador.buscar_por_actor.connect(self.abrir_busqueda_por_actor)

    def mostrar_pantalla(self):
        self.__buscador.show()

    @Slot(str)
    def buscar_pelicula(self, nombre_pelicula):
        coincidencias = self.__catalogo.buscar_pelicula(nombre_pelicula)
        self.__buscador.actualizar_lista_resultados(
            [pelicula.obtener_atributos()["titulo"] for pelicula in coincidencias]
        )

    @Slot(str)
    def mostrar_info_pelicula(self, titulo_pelicula):
        pelicula = self.__catalogo.obtener_info_pelicula(titulo_pelicula)
        if pelicula:
            self.mostrar_ventana_info(pelicula.obtener_atributos())
        else:
            QMessageBox.warning(
                self.__buscador,
                "Advertencia",
                "No se encontró información de la película seleccionada."
            )

    def mostrar_ventana_info(self, pelicula_atributos):
        self.__ventana_info = VentanaInfo(pelicula_atributos)
        self.__ventana_info.show()

    @Slot()
    def abrir_busqueda_por_actor(self):
        if self.__ventana_actor is None:
            self.__ventana_actor = VentanaBuscarPorActor(self.__catalogo.gestionar_catalogo())
        self.__ventana_actor.show()
