# Rosa Elizabeth Parra Sosa Tarea5
# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Tarea5.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_StudentsRegister(object):
    def setupUi(self, StudentsRegister):
        if not StudentsRegister.objectName():
            StudentsRegister.setObjectName(u"StudentsRegister")
        StudentsRegister.resize(314, 609)
        self.centralwidget = QWidget(StudentsRegister)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(20, 30, 281, 291))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamily(u"Bodoni MT")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)

        self.verticalLayout.addWidget(self.label)

        self.label_2 = QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.Nombre_LEdit = QLineEdit(self.verticalLayoutWidget)
        self.Nombre_LEdit.setObjectName(u"Nombre_LEdit")

        self.verticalLayout.addWidget(self.Nombre_LEdit)

        self.label_3 = QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.Apellido_LEdit = QLineEdit(self.verticalLayoutWidget)
        self.Apellido_LEdit.setObjectName(u"Apellido_LEdit")

        self.verticalLayout.addWidget(self.Apellido_LEdit)

        self.label_4 = QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout.addWidget(self.label_4)

        self.Correo_LEdit = QLineEdit(self.verticalLayoutWidget)
        self.Correo_LEdit.setObjectName(u"Correo_LEdit")

        self.verticalLayout.addWidget(self.Correo_LEdit)

        self.label_5 = QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout.addWidget(self.label_5)

        self.Con_LEdit = QLineEdit(self.verticalLayoutWidget)
        self.Con_LEdit.setObjectName(u"Con_LEdit")

        self.verticalLayout.addWidget(self.Con_LEdit)

        self.Registrar = QPushButton(self.verticalLayoutWidget)
        self.Registrar.setObjectName(u"Registrar")

        self.verticalLayout.addWidget(self.Registrar)

        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 380, 293, 41))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.Buscar = QPushButton(self.horizontalLayoutWidget)
        self.Buscar.setObjectName(u"Buscar")

        self.horizontalLayout.addWidget(self.Buscar)

        self.Actualizar = QPushButton(self.horizontalLayoutWidget)
        self.Actualizar.setObjectName(u"Actualizar")

        self.horizontalLayout.addWidget(self.Actualizar)

        self.Eliminar = QPushButton(self.horizontalLayoutWidget)
        self.Eliminar.setObjectName(u"Eliminar")

        self.horizontalLayout.addWidget(self.Eliminar)

        self.Referencia = QLineEdit(self.centralwidget)
        self.Referencia.setObjectName(u"Referencia")
        self.Referencia.setGeometry(QRect(20, 350, 271, 20))
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(20, 330, 181, 16))
        self.cuadro = QTextEdit(self.centralwidget)
        self.cuadro.setObjectName(u"cuadro")
        self.cuadro.setGeometry(QRect(20, 430, 281, 131))
        StudentsRegister.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(StudentsRegister)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 314, 22))
        self.menuRegistro_de_Estudiantes = QMenu(self.menubar)
        self.menuRegistro_de_Estudiantes.setObjectName(u"menuRegistro_de_Estudiantes")
        StudentsRegister.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(StudentsRegister)
        self.statusbar.setObjectName(u"statusbar")
        StudentsRegister.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuRegistro_de_Estudiantes.menuAction())

        self.retranslateUi(StudentsRegister)

        QMetaObject.connectSlotsByName(StudentsRegister)
    # setupUi

    def retranslateUi(self, StudentsRegister):
        StudentsRegister.setWindowTitle(QCoreApplication.translate("StudentsRegister", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("StudentsRegister", u"Nuevo Estudiante", None))
        self.label_2.setText(QCoreApplication.translate("StudentsRegister", u"Nombre:", None))
        self.label_3.setText(QCoreApplication.translate("StudentsRegister", u"Apellido:", None))
        self.label_4.setText(QCoreApplication.translate("StudentsRegister", u"Correo Electr\u00f3nico", None))
        self.label_5.setText(QCoreApplication.translate("StudentsRegister", u"Contrase\u00f1a", None))
        self.Registrar.setText(QCoreApplication.translate("StudentsRegister", u"Registrar", None))
        self.Buscar.setText(QCoreApplication.translate("StudentsRegister", u"Buscar", None))
        self.Actualizar.setText(QCoreApplication.translate("StudentsRegister", u"Actualizar", None))
        self.Eliminar.setText(QCoreApplication.translate("StudentsRegister", u"Eliminar", None))
        self.label_6.setText(QCoreApplication.translate("StudentsRegister", u"Nombre del Usuario a buscar", None))
        self.menuRegistro_de_Estudiantes.setTitle(QCoreApplication.translate("StudentsRegister", u"Registro de Estudiantes", None))
    # retranslateUi
