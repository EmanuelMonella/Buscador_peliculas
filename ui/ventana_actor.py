from PySide6.QtWidgets import QWidget, QMessageBox
from ui.pantalla_actor import Ui_actor


class VentanaBuscarPorActor(QWidget):
    def __init__(self, catalogo):
        super().__init__()
        self.__ui = Ui_actor()
        self.__ui.setupUi(self)
        self.__catalogo = catalogo

        self.__ui.boton_buscar.clicked.connect(self.__buscar_actor)

    def __buscar_actor(self):
        actores_input = self.__ui.input_busqueda.text().strip()
        self.__ui.resultados.clear()
        if actores_input:
            actores = [actor.strip().lower() for actor in actores_input.split(',')]
            coincidencias = [
                pelicula for pelicula in self.__catalogo if
                all(any(actor in a.lower() for a in pelicula.obtener_atributos()["actores"]) for actor in actores)
            ]
            if coincidencias:
                for pelicula in coincidencias:
                    self.__ui.resultados.addItem(pelicula.obtener_atributos()["titulo"])
            else:
                QMessageBox.information(self, "Resultado", "No se encontraron películas para esos actores.")
        else:
            QMessageBox.warning(self, "Advertencia", "Por favor, ingrese los nombres de los actores.")
