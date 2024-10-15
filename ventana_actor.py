from PySide6.QtWidgets import QWidget, QMessageBox, QListWidget
from pantalla_actor import Ui_actor  # Asegúrate de que este import sea correcto


class VentanaBuscarPorActor(QWidget):
    def __init__(self, catalogo):
        super().__init__()
        self.ui = Ui_actor()
        self.ui.setupUi(self)
        self.catalogo = catalogo

    def __buscar_actor(self):
        actores_input = self.ui.input_busqueda.text().strip().lower()
        self.ui.resultados.clear()  # Limpiar resultados del QListWidget
        if actores_input:
            actores = [actor.strip() for actor in actores_input.split(',')]
            coincidencias = [p for p in self.catalogo if
                             all(any(actor in a.lower() for a in p.get('actores', [])) for actor in actores)]
            if coincidencias:
                for pelicula in coincidencias:
                    self.ui.resultados.addItem(pelicula['titulo'])  # Añadir películas al QListWidget
            else:
                QMessageBox.information(self, "Resultado", "No se encontraron películas para esos actores.")
        else:
            QMessageBox.warning(self, "Advertencia", "Por favor, ingrese los nombres de los actores.")
