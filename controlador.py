from PySide6.QtWidgets import QWidget, QMessageBox, QListWidgetItem
from ui.buscador import Ui_Buscador
from ui.ventana_actor import VentanaBuscarPorActor
from ui.ventana_info import VentanaInfo
from ui.catalogo import Controlador

class BuscadorPeliculas(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Buscador()
        self.ui.setupUi(self)
        self.controlador = Controlador()



    def __buscar_pelicula(self):
        nombre_pelicula = self.ui.input_pelicula.text().strip()
        self.ui.lista_resutado.clear()
        if nombre_pelicula:
            coincidencias = self.controlador.buscar_pelicula(nombre_pelicula)
            if coincidencias:
                for pelicula in coincidencias:
                    item = QListWidgetItem(pelicula.titulo)
                    item.setData(1, pelicula)
                    self.ui.lista_resutado.addItem(item)
            else:
                QMessageBox.information(self, "Resultado", "No se encontraron coincidencias.")
        else:
            QMessageBox.warning(self, "Advertencia", "Por favor, ingrese un nombre de película.")

    def __mostrar_info_pelicula(self):
        item = self.ui.lista_resutado.currentItem()
        if item and isinstance(item, QListWidgetItem):
            pelicula = item.data(1)
            if pelicula:
                self.ventana_info = VentanaInfo(pelicula)
                self.ventana_info.show()
        else:
            QMessageBox.warning(self, "Advertencia", "Por favor, seleccione una película.")

    def __abrir_busqueda_por_actor(self):
        self.ventana_actor = VentanaBuscarPorActor(self.controlador.catalogo)
        self.ventana_actor.show()
