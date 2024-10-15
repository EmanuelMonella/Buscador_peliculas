from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
from PySide6.QtGui import QPixmap

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
        self.label_sinopsis = QLabel(f"<b>Sinopsis:</b> {pelicula['sinopsis']}")
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


