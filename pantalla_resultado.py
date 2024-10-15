# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pantalla_resultado.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QPlainTextEdit, QSizePolicy, QWidget)

class Ui_info_peliculas(object):
    def setupUi(self, info_peliculas):
        if not info_peliculas.objectName():
            info_peliculas.setObjectName(u"info_peliculas")
        info_peliculas.resize(400, 300)
        self.gridLayout = QGridLayout(info_peliculas)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_actores = QLabel(info_peliculas)
        self.label_actores.setObjectName(u"label_actores")

        self.gridLayout.addWidget(self.label_actores, 4, 0, 1, 1)

        self.label_titulo = QLabel(info_peliculas)
        self.label_titulo.setObjectName(u"label_titulo")

        self.gridLayout.addWidget(self.label_titulo, 0, 0, 1, 1)

        self.label_puntuacion = QLabel(info_peliculas)
        self.label_puntuacion.setObjectName(u"label_puntuacion")

        self.gridLayout.addWidget(self.label_puntuacion, 5, 0, 1, 1)

        self.label_sinopsis = QLabel(info_peliculas)
        self.label_sinopsis.setObjectName(u"label_sinopsis")

        self.gridLayout.addWidget(self.label_sinopsis, 2, 0, 1, 1)

        self.resultado_titulo = QLineEdit(info_peliculas)
        self.resultado_titulo.setObjectName(u"resultado_titulo")

        self.gridLayout.addWidget(self.resultado_titulo, 0, 1, 1, 1)

        self.resultado_sinopsis = QPlainTextEdit(info_peliculas)
        self.resultado_sinopsis.setObjectName(u"resultado_sinopsis")

        self.gridLayout.addWidget(self.resultado_sinopsis, 3, 0, 1, 2)

        self.resultado_actores = QLineEdit(info_peliculas)
        self.resultado_actores.setObjectName(u"resultado_actores")

        self.gridLayout.addWidget(self.resultado_actores, 4, 1, 1, 1)

        self.resultado_puntuacion = QLineEdit(info_peliculas)
        self.resultado_puntuacion.setObjectName(u"resultado_puntuacion")

        self.gridLayout.addWidget(self.resultado_puntuacion, 5, 1, 1, 1)

        self.label_poster = QLabel(info_peliculas)
        self.label_poster.setObjectName(u"label_poster")

        self.gridLayout.addWidget(self.label_poster, 6, 0, 1, 2)


        self.retranslateUi(info_peliculas)

        QMetaObject.connectSlotsByName(info_peliculas)
    # setupUi

    def retranslateUi(self, info_peliculas):
        info_peliculas.setWindowTitle(QCoreApplication.translate("info_peliculas", u"Form", None))
        self.label_actores.setText(QCoreApplication.translate("info_peliculas", u"Actores:", None))
        self.label_titulo.setText(QCoreApplication.translate("info_peliculas", u"Titulo: ", None))
        self.label_puntuacion.setText(QCoreApplication.translate("info_peliculas", u"Puntuacion:", None))
        self.label_sinopsis.setText(QCoreApplication.translate("info_peliculas", u"Sinopsis:", None))
        self.label_poster.setText("")
    # retranslateUi

