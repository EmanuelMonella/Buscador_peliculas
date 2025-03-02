from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QPixmap
from ui.pantalla_resultado import Ui_info_peliculas
from PySide6.QtCore import QSize

class VentanaInfo(QWidget):
    def __init__(self, pelicula_atributos):
        super().__init__()
        self.__ui = Ui_info_peliculas()
        self.__ui.setupUi(self)
        self.setWindowTitle("Resultado")
        self.__ui.resultado_titulo.setText(pelicula_atributos["titulo"])
        actores = ", ".join(pelicula_atributos["actores"])
        self.__ui.resultado_actores.setText(actores)
        self.__ui.resultado_sinopsis.setPlainText(pelicula_atributos["sinopsis"])
        self.__ui.resultado_puntuacion.setText(str(pelicula_atributos["puntuacion"]))
        if pelicula_atributos["poster"]:
            self.__ui.label_poster.setFixedSize(QSize(200, 300))
            pixmap = QPixmap(pelicula_atributos["poster"])
            if not pixmap.isNull():
                self.__ui.label_poster.setPixmap(pixmap)
                self.__ui.label_poster.setScaledContents(True)
            else:
                self.__ui.label_poster.setText("Imagen no disponible")
        else:
            self.__ui.label_poster.setText("Sin póster disponible")
