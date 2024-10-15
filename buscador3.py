# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'buscador3.ui'
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
    QListWidget, QListWidgetItem, QPushButton, QSizePolicy,
    QSpacerItem, QWidget)

class Ui_Buscador(object):
    def setupUi(self, Buscador):
        if not Buscador.objectName():
            Buscador.setObjectName(u"Buscador")
        Buscador.resize(400, 300)
        self.gridLayout = QGridLayout(Buscador)
        self.gridLayout.setObjectName(u"gridLayout")
        self.info = QPushButton(Buscador)
        self.info.setObjectName(u"info")

        self.gridLayout.addWidget(self.info, 5, 2, 1, 1)

        self.lista_resutado = QListWidget(Buscador)
        self.lista_resutado.setObjectName(u"lista_resutado")

        self.gridLayout.addWidget(self.lista_resutado, 3, 0, 1, 3)

        self.label_pelicula = QLabel(Buscador)
        self.label_pelicula.setObjectName(u"label_pelicula")

        self.gridLayout.addWidget(self.label_pelicula, 0, 0, 1, 1)

        self.boton_buscar_pelicula = QPushButton(Buscador)
        self.boton_buscar_pelicula.setObjectName(u"boton_buscar_pelicula")

        self.gridLayout.addWidget(self.boton_buscar_pelicula, 1, 2, 1, 1)

        self.input_pelicula = QLineEdit(Buscador)
        self.input_pelicula.setObjectName(u"input_pelicula")

        self.gridLayout.addWidget(self.input_pelicula, 1, 0, 1, 1)

        self.boton_actor = QPushButton(Buscador)
        self.boton_actor.setObjectName(u"boton_actor")

        self.gridLayout.addWidget(self.boton_actor, 5, 0, 1, 1)

        self.label_resultado = QLabel(Buscador)
        self.label_resultado.setObjectName(u"label_resultado")

        self.gridLayout.addWidget(self.label_resultado, 2, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 5, 1, 1, 1)


        self.retranslateUi(Buscador)
        self.boton_buscar_pelicula.clicked.connect(Buscador._BuscadorPeliculas__buscar_pelicula)

        QMetaObject.connectSlotsByName(Buscador)
    # setupUi

    def retranslateUi(self, Buscador):
        Buscador.setWindowTitle(QCoreApplication.translate("Buscador", u"Buscador de peliculas", None))
        self.info.setText(QCoreApplication.translate("Buscador", u"Descri\u1e55cion", None))
        self.label_pelicula.setText(QCoreApplication.translate("Buscador", u"Ingrese el nombre de la pelicula:", None))
        self.boton_buscar_pelicula.setText(QCoreApplication.translate("Buscador", u"Buscar", None))
        self.boton_actor.setText(QCoreApplication.translate("Buscador", u"Buscar por actor", None))
        self.label_resultado.setText(QCoreApplication.translate("Buscador", u"Resultado:", None))
    # retranslateUi

