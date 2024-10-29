from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QPixmap
from ui.pantalla_resultado import Ui_info_peliculas
from PySide6.QtCore import QSize


class VentanaInfo(QWidget):
    def __init__(self, pelicula):
        super().__init__()
        self.ui = Ui_info_peliculas()
        self.ui.setupUi(self)
        self.ui.resultado_titulo.setText(pelicula.titulo)
        actores = ", ".join(pelicula.actores)
        self.ui.resultado_actores.setText(actores)
        self.ui.resultado_sinopsis.setPlainText(pelicula.sinopsis)
        self.ui.resultado_puntuacion.setText(str(pelicula.puntuacion))

        if pelicula.poster:
            self.ui.label_poster.setFixedSize(QSize(200, 300))
            self.ui.label_poster.setPixmap(QPixmap(pelicula.poster))
            self.ui.label_poster.setScaledContents(True)