from PySide6.QtWidgets import QWidget, QMessageBox, QListWidgetItem
from ui.buscador import Ui_Buscador
from ui.ventana_actor import VentanaBuscarPorActor
from ui.ventana_info import VentanaInfo
from controlador import Controlador

class BuscadorPeliculas(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Buscador()
        self.ui.setupUi(self)
        self.controlador = Controlador()

        self.ui.boton_buscar_pelicula.clicked.connect(self.__buscar_pelicula)
        self.ui.lista_resutado.itemDoubleClicked.connect(self.__mostrar_info_pelicula)
        self.ui.boton_actor.clicked.connect(self.__abrir_busqueda_por_actor)

    def __buscar_pelicula(self):
        nombre_pelicula = self.ui.input_pelicula.text().strip()
        mensaje = self.controlador.manejar_busqueda(nombre_pelicula, self.ui.lista_resutado)
        if mensaje:
            QMessageBox.information(self, "Resultado", mensaje)

    def __mostrar_info_pelicula(self):
        item = self.ui.lista_resutado.currentItem()
        pelicula = self.controlador.mostrar_info_pelicula(item)
        if pelicula:
            self.ventana_info = VentanaInfo(pelicula)
            self.ventana_info.show()
        else:
            QMessageBox.warning(self, "Advertencia", "Por favor, seleccione una película.")

    def __abrir_busqueda_por_actor(self):
        self.ventana_actor = VentanaBuscarPorActor(self.controlador.catalogo)
        self.ventana_actor.show()
