import json
from PySide6.QtWidgets import QWidget, QMessageBox,QListWidgetItem
from buscador import Ui_Buscador
from ventana_actor import VentanaBuscarPorActor
from ventana_info import VentanaInfo

class BuscadorPeliculas(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Buscador()
        self.ui.setupUi(self)
        self.__catalogo = self.__cargar_catalogo()

    def __cargar_catalogo(self):
        with open('peliculas/catalogo.json', 'r') as file:
            return json.load(file)

    def __buscar_pelicula(self):
        nombre_pelicula = self.ui.input_pelicula.text().strip().lower()
        self.ui.lista_resutado.clear()
        if nombre_pelicula:
            coincidencias = [p for p in self.__catalogo if nombre_pelicula in p['titulo'].lower()]
            if coincidencias:
                for pelicula in coincidencias:
                    item = QListWidgetItem(pelicula['titulo'])
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
        self.ventana_actor = VentanaBuscarPorActor(self.__catalogo)
        self.ventana_actor.show()
