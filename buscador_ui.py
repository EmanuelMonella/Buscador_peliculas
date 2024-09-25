# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'buscador_ui.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLineEdit, QListWidget,
    QListWidgetItem, QPushButton, QSizePolicy, QSpacerItem,
    QWidget)

class Ui_buscador(object):
    def setupUi(self, buscador):
        if not buscador.objectName():
            buscador.setObjectName(u"buscador")
        buscador.resize(340, 371)
        buscador.setMaximumSize(QSize(640, 480))
        self.gridLayout = QGridLayout(buscador)
        self.gridLayout.setObjectName(u"gridLayout")
        self.boton_buscar = QPushButton(buscador)
        self.boton_buscar.setObjectName(u"boton_buscar")

        self.gridLayout.addWidget(self.boton_buscar, 0, 2, 1, 1)

        self.lista_resultado = QListWidget(buscador)
        self.lista_resultado.setObjectName(u"lista_resultado")

        self.gridLayout.addWidget(self.lista_resultado, 1, 0, 1, 3)

        self.buscador_input = QLineEdit(buscador)
        self.buscador_input.setObjectName(u"buscador_input")

        self.gridLayout.addWidget(self.buscador_input, 0, 0, 1, 1)

        self.boton_resultado = QPushButton(buscador)
        self.boton_resultado.setObjectName(u"boton_resultado")

        self.gridLayout.addWidget(self.boton_resultado, 2, 0, 1, 3)

        self.boton_actor = QPushButton(buscador)
        self.boton_actor.setObjectName(u"boton_actor")

        self.gridLayout.addWidget(self.boton_actor, 3, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 3, 1, 1, 2)


        self.retranslateUi(buscador)

        QMetaObject.connectSlotsByName(buscador)
    # setupUi

    def retranslateUi(self, buscador):
        buscador.setWindowTitle(QCoreApplication.translate("buscador", u"Form", None))
        self.boton_buscar.setText(QCoreApplication.translate("buscador", u"Buscar", None))
        self.buscador_input.setPlaceholderText(QCoreApplication.translate("buscador", u"Introduzca la pelicula", None))
        self.boton_resultado.setText(QCoreApplication.translate("buscador", u"Descripcion", None))
        self.boton_actor.setText(QCoreApplication.translate("buscador", u"Buscar por actor", None))
    # retranslateUi

