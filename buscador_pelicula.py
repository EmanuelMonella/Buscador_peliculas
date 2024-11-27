from PySide6.QtCore import Signal
from PySide6.QtWidgets import QWidget, QMessageBox
from ui.buscador import Ui_Buscador


class BuscadorPeliculas(QWidget):
    buscar_pelicula_signal = Signal(str)
    mostrar_info_pelicula_signal = Signal(str)
    buscar_por_actor_signal = Signal()

    def __init__(self):
        super().__init__()
        self.ui = Ui_Buscador()
        self.ui.setupUi(self)

        # Conexión de botones a señales
        self.ui.boton_buscar_pelicula.clicked.connect(self.__emitir_busqueda)
        self.ui.info.clicked.connect(self.__emitir_info_pelicula)
        self.ui.boton_actor.clicked.connect(self.__emitir_busqueda_por_actor)

    def __emitir_busqueda(self):
        nombre_pelicula = self.ui.input_pelicula.text().strip()
        self.buscar_pelicula_signal.emit(nombre_pelicula)

    def __emitir_info_pelicula(self):
        item = self.ui.lista_resutado.currentItem()
        if item:
            titulo = item.text().strip()
            self.mostrar_info_pelicula_signal.emit(titulo)
        else:
            QMessageBox.warning(self, "Advertencia", "Por favor, seleccione una película.")

    def __emitir_busqueda_por_actor(self):
        self.buscar_por_actor_signal.emit()

    def actualizar_lista_resultados(self, titulos):
        self.ui.lista_resutado.clear()
        for titulo in titulos:
            self.ui.lista_resutado.addItem(titulo)
