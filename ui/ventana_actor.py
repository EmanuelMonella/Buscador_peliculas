from PySide6.QtWidgets import QWidget, QMessageBox, QListWidgetItem
from PySide6.QtCore import Signal
from ui.pantalla_actor import Ui_actor

class VentanaBuscarPorActor(QWidget):
    buscar_actor = Signal(str)
    mostrar_info_pelicula = Signal(str)

    def __init__(self, catalogo):
        super().__init__()
        self.__ui = Ui_actor()
        self.__ui.setupUi(self)

        self.__ui.boton_buscar.clicked.connect(self.__emitir_busqueda)
        self.__ui.resultados.itemDoubleClicked.connect(self.__mostrar_info_pelicula)

    def __emitir_busqueda(self):
        actores_input = self.__ui.input_busqueda.text().strip()
        if actores_input:
            self.buscar_actor.emit(actores_input)
        else:
            QMessageBox.warning(self, "Advertencia", "Por favor, ingrese los nombres de los actores.")

    def actualizar_resultados(self, titulos):
        self.__ui.resultados.clear()
        for titulo in titulos:
            self.__ui.resultados.addItem(titulo)

    def __mostrar_info_pelicula(self, item: QListWidgetItem):
        titulo_pelicula = item.text()
        self.mostrar_info_pelicula.emit(titulo_pelicula)
