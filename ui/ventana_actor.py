from PySide6.QtWidgets import QWidget, QMessageBox
from ui.pantalla_actor import Ui_actor


class VentanaBuscarPorActor(QWidget):
    def __init__(self, catalogo):
        super().__init__()
        self.ui = Ui_actor()
        self.ui.setupUi(self)
        self.catalogo = catalogo


    def __buscar_actor(self):
        actores_input = self.ui.input_busqueda.text().strip()
        self.ui.resultados.clear()
        if actores_input:
            coincidencias = [pelicula for pelicula in self.catalogo if
                             any(actor in pelicula.actores for actor in actores_input.split(','))]
            if coincidencias:
                for pelicula in coincidencias:
                    self.ui.resultados.addItem(pelicula.titulo)
            else:
                QMessageBox.information(self, "Resultado", "No se encontraron películas para esos actores.")
        else:
            QMessageBox.warning(self, "Advertencia", "Por favor, ingrese los nombres de los actores.")
