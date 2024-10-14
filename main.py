import sys
import json
from PySide6.QtWidgets import QApplication, QWidget, QMessageBox, QVBoxLayout, QLabel, QLineEdit, QPushButton, \
    QListWidget, QListWidgetItem
from PySide6.QtGui import QPixmap
from buscador2 import Ui_Buscador

#Pasar todo a privado, separar ventanas, pasar a mvc, poner posters



class BuscadorPeliculas(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Buscador()
        self.ui.setupUi(self)
        self.catalogo = self.cargar_catalogo()
        #MMMMMM Mandar botones designer
        self.ui.boton_buscar_pelicula.clicked.connect(self.buscar_pelicula)
        self.ui.boton_actor.clicked.connect(self.abrir_busqueda_por_actor)
        self.ui.info.clicked.connect(self.mostrar_info_pelicula)

    def cargar_catalogo(self):
        with open('catalogo.json', 'r', encoding='utf-8') as file:
            return json.load(file)

    def buscar_pelicula(self):
        nombre_pelicula = self.ui.input_pelicula.text().strip().lower()
        self.ui.lista_resutado.clear()
        if nombre_pelicula:
            coincidencias = [p for p in self.catalogo if nombre_pelicula in p['titulo'].lower()]
            if coincidencias:
                for pelicula in coincidencias:
                    item = QListWidgetItem(pelicula['titulo'])
                    item.setData(1, pelicula)
                    self.ui.lista_resutado.addItem(item)
            else:
                QMessageBox.information(self, "Resultado", "No se encontraron coincidencias.")
        else:
            QMessageBox.warning(self, "Advertencia", "Por favor, ingrese un nombre de película.")

    def mostrar_info_pelicula(self):
        item = self.ui.lista_resutado.currentItem()
        if item and isinstance(item, QListWidgetItem):
            pelicula = item.data(1)
            if pelicula:
                self.ventana_info = VentanaInfo(pelicula)
                self.ventana_info.show()
        else:
            QMessageBox.warning(self, "Advertencia", "Por favor, seleccione una película.")

    def abrir_busqueda_por_actor(self):
        self.ventana_actor = VentanaBuscarPorActor(self.catalogo)
        self.ventana_actor.show()


class VentanaInfo(QWidget):
    def __init__(self, pelicula):
        super().__init__()
        self.setWindowTitle("Información de la Película")
        self.setGeometry(100, 100, 400, 400)
        layout = QVBoxLayout()
        self.label_titulo = QLabel(f"<b>Título:</b> {pelicula['titulo']}")
        layout.addWidget(self.label_titulo)
        actores = ", ".join(pelicula.get('actores', ['No hay actores disponibles']))
        self.label_actores = QLabel(f"<b>Actores:</b> {actores}")
        layout.addWidget(self.label_actores)
        self.label_sinopsis = QLabel(f"<b>Sinopsis:</b> {pelicula.get('sinopsis', 'No hay sinopsis disponible.')}")
        layout.addWidget(self.label_sinopsis)
        puntuacion = pelicula.get('puntuacion', 'No hay puntuación disponible.')
        self.label_puntuacion = QLabel(f"<b>Puntuación:</b> {puntuacion}")
        layout.addWidget(self.label_puntuacion)
        if 'poster' in pelicula:
            self.label_poster = QLabel()
            self.label_poster.setPixmap(QPixmap(pelicula['poster']))
            self.label_poster.setScaledContents(True)
            layout.addWidget(self.label_poster)
        self.setLayout(layout)


class VentanaBuscarPorActor(QWidget):
    def __init__(self, catalogo):
        super().__init__()
        self.setWindowTitle("Buscar Películas por Actor")
        self.setGeometry(100, 100, 300, 200)
        self.catalogo = catalogo
        layout = QVBoxLayout()
        self.label_actor = QLabel("Ingrese los nombres de los actores (separados por coma):")
        layout.addWidget(self.label_actor)
        self.input_actor = QLineEdit()
        layout.addWidget(self.input_actor)
        self.boton_buscar_actor = QPushButton("Buscar")
        self.boton_buscar_actor.clicked.connect(self.buscar_actor)
        layout.addWidget(self.boton_buscar_actor)
        self.lista_resultados_actor = QListWidget()
        layout.addWidget(self.lista_resultados_actor)
        self.setLayout(layout)

    def buscar_actor(self):
        actores_input = self.input_actor.text().strip().lower()
        self.lista_resultados_actor.clear()
        if actores_input:
            actores = [actor.strip() for actor in actores_input.split(',')]
            coincidencias = [p for p in self.catalogo if all(any(actor in a.lower() for a in p.get('actores', [])) for actor in actores)]
            if coincidencias:
                for pelicula in coincidencias:
                    self.lista_resultados_actor.addItem(pelicula['titulo'])
            else:
                QMessageBox.information(self, "Resultado", "No se encontraron películas para esos actores.")
        else:
            QMessageBox.warning(self, "Advertencia", "Por favor, ingrese los nombres de los actores.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = BuscadorPeliculas()
    ventana.show()
    sys.exit(app.exec())
