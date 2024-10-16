# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pantalla_actor.ui'
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
    QWidget)

class Ui_actor(object):
    def setupUi(self, actor):
        if not actor.objectName():
            actor.setObjectName(u"actor")
        actor.setWindowModality(Qt.WindowModality.NonModal)
        actor.resize(422, 184)
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.UserAvailable))
        actor.setWindowIcon(icon)
        self.gridLayout = QGridLayout(actor)
        self.gridLayout.setObjectName(u"gridLayout")
        self.boton_buscar = QPushButton(actor)
        self.boton_buscar.setObjectName(u"boton_buscar")

        self.gridLayout.addWidget(self.boton_buscar, 2, 0, 1, 1)

        self.input_busqueda = QLineEdit(actor)
        self.input_busqueda.setObjectName(u"input_busqueda")

        self.gridLayout.addWidget(self.input_busqueda, 1, 0, 1, 1)

        self.label_busqueda = QLabel(actor)
        self.label_busqueda.setObjectName(u"label_busqueda")

        self.gridLayout.addWidget(self.label_busqueda, 0, 0, 1, 1)

        self.resultados = QListWidget(actor)
        self.resultados.setObjectName(u"resultados")

        self.gridLayout.addWidget(self.resultados, 3, 0, 1, 1)


        self.retranslateUi(actor)
        self.boton_buscar.clicked.connect(actor._VentanaBuscarPorActor__buscar_actor)

        QMetaObject.connectSlotsByName(actor)
    # setupUi

    def retranslateUi(self, actor):
        actor.setWindowTitle(QCoreApplication.translate("actor", u"Busqueda por actor", None))
        self.boton_buscar.setText(QCoreApplication.translate("actor", u"Buscar", None))
        self.label_busqueda.setText(QCoreApplication.translate("actor", u"Ingrese el nombre de dos actores (separados por comas):", None))
    # retranslateUi

