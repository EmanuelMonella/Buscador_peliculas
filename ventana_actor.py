from PySide6.QtWidgets import QWidget, QMessageBox, QVBoxLayout, QLabel, QLineEdit, QPushButton, \
    QListWidget

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