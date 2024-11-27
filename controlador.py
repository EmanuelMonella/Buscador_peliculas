from PySide6.QtCore import Slot
from PySide6.QtWidgets import QMessageBox
from ui.catalogo import Catalogo
from buscador_pelicula import BuscadorPeliculas
from ui.ventana_actor import VentanaBuscarPorActor
from ui.ventana_info import VentanaInfo


class Controlador:
    def __init__(self):
        self.catalogo = Catalogo()
        self.buscador = BuscadorPeliculas()
        self.ventana_actor = None
        self.ventana_info = None

        self.buscador.buscar_pelicula_signal.connect(self.slot_buscar_pelicula)
        self.buscador.mostrar_info_pelicula_signal.connect(self.slot_mostrar_info_pelicula)
        self.buscador.buscar_por_actor_signal.connect(self.slot_abrir_busqueda_por_actor)

        self.buscador.show()

    @Slot(str)
    def slot_buscar_pelicula(self, nombre_pelicula):
        coincidencias = self.catalogo.buscar_pelicula(nombre_pelicula)
        self.buscador.ui.lista_resutado.clear()
        if coincidencias:
            self.buscador.actualizar_lista_resultados([p.titulo for p in coincidencias])
        else:
            QMessageBox.information(self.buscador, "Resultado", "No se encontraron coincidencias.")

    @Slot(str)
    def slot_mostrar_info_pelicula(self, titulo_pelicula):
        pelicula = self.catalogo.obtener_info_pelicula(titulo_pelicula)
        if pelicula:
            self.mostrar_ventana_info(pelicula)
        else:
            QMessageBox.warning(self.buscador, "Advertencia", "No se encontró información de la película seleccionada.")

    def mostrar_ventana_info(self, pelicula):
        self.ventana_info = VentanaInfo(pelicula)
        self.ventana_info.show()

    @Slot()
    def slot_abrir_busqueda_por_actor(self):
        if self.ventana_actor is None:
            self.ventana_actor = VentanaBuscarPorActor(self.catalogo.catalogo)
        self.ventana_actor.show()
