from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QPixmap
from ui.pantalla_resultado import Ui_info_peliculas


class VentanaInfo(QWidget):
    def __init__(self, pelicula):
        super().__init__()
        self.ui = Ui_info_peliculas()
        self.ui.setupUi(self)
        self.ui.resultado_titulo.setText(pelicula['titulo'])
        actores = ", ".join(pelicula.get('actores', ['No hay actores disponibles']))
        self.ui.resultado_actores.setText(actores)
        self.ui.resultado_sinopsis.setPlainText(pelicula['sinopsis'])
        puntuacion = pelicula.get('puntuacion', 'No hay puntuación disponible.')
        self.ui.resultado_puntuacion.setText(str(puntuacion))
        if 'poster' in pelicula:
            self.ui.label_poster.setPixmap(QPixmap(pelicula['poster']))
            self.ui.label_poster.setScaledContents(True)
