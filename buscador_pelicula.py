from PySide6.QtCore import Signal
from PySide6.QtWidgets import QWidget, QMessageBox
from ui.buscador import Ui_Buscador


class BuscadorPeliculas(QWidget):
    # Señales
    buscar_pelicula_signal = Signal(str)  # Emitirá el nombre de la película a buscar
    mostrar_info_pelicula_signal = Signal(str)  # Emitirá el título de la película seleccionada
    buscar_por_actor_signal = Signal()  # Nueva señal para búsqueda por actor

    def __init__(self):
        super().__init__()
        self.ui = Ui_Buscador()
        self.ui.setupUi(self)

        # Conexión de botones a señales
        self.ui.boton_buscar_pelicula.clicked.connect(self.__emitir_busqueda)
        self.ui.info.clicked.connect(self.__emitir_info_pelicula)
        self.ui.boton_actor.clicked.connect(self.__emitir_busqueda_por_actor)

    def __emitir_busqueda(self):
        """
        Emite la señal para buscar una película basada en el texto ingresado.
        """
        nombre_pelicula = self.ui.input_pelicula.text().strip()
        self.buscar_pelicula_signal.emit(nombre_pelicula)

    def __emitir_info_pelicula(self):
        """
        Emite la señal para mostrar información sobre la película seleccionada.
        """
        item = self.ui.lista_resutado.currentItem()
        if item:
            titulo = item.text().strip()
            self.mostrar_info_pelicula_signal.emit(titulo)
        else:
            QMessageBox.warning(self, "Advertencia", "Por favor, seleccione una película.")

    def __emitir_busqueda_por_actor(self):
        """
        Emite la señal para abrir la búsqueda por actor.
        """
        self.buscar_por_actor_signal.emit()

    def actualizar_lista_resultados(self, titulos):
        """
        Actualiza la lista de resultados con los títulos proporcionados.
        """
        self.ui.lista_resutado.clear()
        for titulo in titulos:
            self.ui.lista_resutado.addItem(titulo)
