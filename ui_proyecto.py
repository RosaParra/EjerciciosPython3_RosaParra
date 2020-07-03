# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'proyecto.ui'
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


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(335, 457)
        font = QFont()
        font.setFamily(u"MS Shell Dlg 2")
        MainWindow.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.Servidor = QGroupBox(self.centralwidget)
        self.Servidor.setObjectName(u"Servidor")
        self.Servidor.setGeometry(QRect(20, 10, 301, 101))
        self.horizontalLayoutWidget = QWidget(self.Servidor)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(9, 20, 281, 41))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.IP_Label = QLabel(self.horizontalLayoutWidget)
        self.IP_Label.setObjectName(u"IP_Label")

        self.horizontalLayout.addWidget(self.IP_Label)

        self.IP = QLineEdit(self.horizontalLayoutWidget)
        self.IP.setObjectName(u"IP")

        self.horizontalLayout.addWidget(self.IP)

        self.Puerto_Label = QLabel(self.horizontalLayoutWidget)
        self.Puerto_Label.setObjectName(u"Puerto_Label")

        self.horizontalLayout.addWidget(self.Puerto_Label)

        self.Puerto = QLineEdit(self.horizontalLayoutWidget)
        self.Puerto.setObjectName(u"Puerto")

        self.horizontalLayout.addWidget(self.Puerto)

        self.Conectar = QPushButton(self.Servidor)
        self.Conectar.setObjectName(u"Conectar")
        self.Conectar.setGeometry(QRect(10, 70, 281, 21))
        self.Conectar.setCheckable(True)
        self.Conectar.setChecked(True)
        self.Estudiante = QGroupBox(self.centralwidget)
        self.Estudiante.setObjectName(u"Estudiante")
        self.Estudiante.setGeometry(QRect(20, 120, 301, 181))
        self.horizontalLayoutWidget_2 = QWidget(self.Estudiante)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(10, 20, 281, 31))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.Nombre_Label = QLabel(self.horizontalLayoutWidget_2)
        self.Nombre_Label.setObjectName(u"Nombre_Label")

        self.horizontalLayout_2.addWidget(self.Nombre_Label)

        self.Nombre = QLineEdit(self.horizontalLayoutWidget_2)
        self.Nombre.setObjectName(u"Nombre")

        self.horizontalLayout_2.addWidget(self.Nombre)

        self.horizontalLayoutWidget_3 = QWidget(self.Estudiante)
        self.horizontalLayoutWidget_3.setObjectName(u"horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QRect(10, 60, 281, 31))
        self.horizontalLayout_3 = QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.Correo_Label = QLabel(self.horizontalLayoutWidget_3)
        self.Correo_Label.setObjectName(u"Correo_Label")

        self.horizontalLayout_3.addWidget(self.Correo_Label)

        self.Correo = QLineEdit(self.horizontalLayoutWidget_3)
        self.Correo.setObjectName(u"Correo")

        self.horizontalLayout_3.addWidget(self.Correo)

        self.horizontalLayoutWidget_4 = QWidget(self.Estudiante)
        self.horizontalLayoutWidget_4.setObjectName(u"horizontalLayoutWidget_4")
        self.horizontalLayoutWidget_4.setGeometry(QRect(10, 100, 281, 31))
        self.horizontalLayout_4 = QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.Nombre_Label_2 = QLabel(self.horizontalLayoutWidget_4)
        self.Nombre_Label_2.setObjectName(u"Nombre_Label_2")

        self.horizontalLayout_4.addWidget(self.Nombre_Label_2)

        self.Contrasena = QLineEdit(self.horizontalLayoutWidget_4)
        self.Contrasena.setObjectName(u"Contrasena")

        self.horizontalLayout_4.addWidget(self.Contrasena)

        self.EnviarNombre = QPushButton(self.Estudiante)
        self.EnviarNombre.setObjectName(u"EnviarNombre")
        self.EnviarNombre.setGeometry(QRect(10, 140, 281, 21))
        self.Archivo = QGroupBox(self.centralwidget)
        self.Archivo.setObjectName(u"Archivo")
        self.Archivo.setGeometry(QRect(20, 310, 301, 80))
        self.horizontalLayoutWidget_5 = QWidget(self.Archivo)
        self.horizontalLayoutWidget_5.setObjectName(u"horizontalLayoutWidget_5")
        self.horizontalLayoutWidget_5.setGeometry(QRect(10, 20, 281, 31))
        self.horizontalLayout_5 = QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.Buscar = QPushButton(self.horizontalLayoutWidget_5)
        self.Buscar.setObjectName(u"Buscar")

        self.horizontalLayout_5.addWidget(self.Buscar)

        self.AbrirArchivo = QLineEdit(self.horizontalLayoutWidget_5)
        self.AbrirArchivo.setObjectName(u"AbrirArchivo")

        self.horizontalLayout_5.addWidget(self.AbrirArchivo)

        self.EnviaArchivo = QPushButton(self.Archivo)
        self.EnviaArchivo.setObjectName(u"EnviaArchivo")
        self.EnviaArchivo.setGeometry(QRect(10, 50, 281, 21))
        self.Estado = QLabel(self.centralwidget)
        self.Estado.setObjectName(u"Estado")
        self.Estado.setGeometry(QRect(200, 400, 121, 16))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 335, 21))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Cliente <Rosa Parra>", None))
        self.Servidor.setTitle(QCoreApplication.translate("MainWindow", u"Servidor", None))
        self.IP_Label.setText(QCoreApplication.translate("MainWindow", u"IP:", None))
        self.Puerto_Label.setText(QCoreApplication.translate("MainWindow", u"Puerto:", None))
        self.Conectar.setText(QCoreApplication.translate("MainWindow", u"Conectar", None))
        self.Estudiante.setTitle(QCoreApplication.translate("MainWindow", u"Estudiante", None))
        self.Nombre_Label.setText(QCoreApplication.translate("MainWindow", u"Nombre", None))
        self.Correo_Label.setText(QCoreApplication.translate("MainWindow", u"Correo", None))
        self.Nombre_Label_2.setText(QCoreApplication.translate("MainWindow", u"Contrase\u00f1a", None))
        self.EnviarNombre.setText(QCoreApplication.translate("MainWindow", u"Enviar", None))
        self.Archivo.setTitle(QCoreApplication.translate("MainWindow", u"Archivo", None))
        self.Buscar.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.EnviaArchivo.setText(QCoreApplication.translate("MainWindow", u"Enviar", None))
        self.Estado.setText(QCoreApplication.translate("MainWindow", u"Estado: Desconectado", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"Cliente <Rosa Parra>", None))
    # retranslateUi

