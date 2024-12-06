from PySide6.QtCore import Signal
from PySide6.QtWidgets import QWidget, QMessageBox
from ui.buscador import Ui_Buscador

class BuscadorPeliculas(QWidget):
    buscar_pelicula = Signal(str)
    mostrar_info_pelicula = Signal(str)
    buscar_por_actor = Signal()

    def __init__(self):
        super().__init__()
        self.__ui = Ui_Buscador()
        self.__ui.setupUi(self)

        self.__ui.boton_buscar_pelicula.clicked.connect(self.__emitir_busqueda)
        self.__ui.info.clicked.connect(self.__emitir_info_pelicula)
        self.__ui.boton_actor.clicked.connect(self.__emitir_busqueda_por_actor)

    def __emitir_busqueda(self):
        nombre_pelicula = self.__ui.input_pelicula.text().strip()
        self.buscar_pelicula.emit(nombre_pelicula)

    def __emitir_info_pelicula(self):
        item = self.__ui.lista_resutado.currentItem()
        if item:
            titulo = item.text().strip()
            self.mostrar_info_pelicula.emit(titulo)
        else:
            QMessageBox.warning(self, "Advertencia", "Por favor, seleccione una película.")

    def __emitir_busqueda_por_actor(self):
        self.buscar_por_actor.emit()

    def actualizar_lista_resultados(self, titulos):
        self.__ui.lista_resutado.clear()
        for titulo in titulos:
            self.__ui.lista_resutado.addItem(titulo)
