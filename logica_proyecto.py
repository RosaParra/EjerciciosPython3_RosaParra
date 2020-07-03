from PySide2.QtWidgets import QApplication, QMainWindow, QFileDialog
from PySide2.QtCore import Slot
from ui_proyecto import Ui_MainWindow
from estudiante import Estudiante
import socket as s
import time


es = Estudiante


class MainWindow(QMainWindow):
    def __init__(self):
        super (MainWindow, self). __init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.Conectado = False
        self.cliente = s.socket()



        self.ui.EnviarNombre.clicked.connect(self.enviarObjeto)
        self.ui.Conectar.clicked.connect(self.conexionTCP)
        self.ui.Buscar.clicked.connect(self.abrirArchivo)
        self.ui.EnviaArchivo.clicked.connect(self.enviarArchivo)


    def conexionTCP(self):
        ip0 = f'\'{self.ui.IP.text()}\''
        puerto = int(self.ui.Puerto.text())
        ip = '127.0.0.1'
        print(ip)
        print(puerto)
        if self.Conectado == False:

            # Establecer conexión
            self.cliente.connect((ip, puerto))
            self.ui.Conectar.setText('Desconectar')
            self.ui.Estado.setText('Estado: Conectado')
            print(f'Conectado al servidor')
            data = self.cliente.recv(1024)
            print(f'Recibido: {data}')
            self.Conectado = True
        else:
            self.ui.IP.clear()
            self.ui.Puerto.clear()
            self.ui.Conectar.setText('Conectar')
            self.ui.Estado.setText('Estado: Desconectado')
            self.Conectado = False
            self.puerto = 0
            self.ip = ''




    def enviarObjeto(self):
        #Crear Objeto
        v = Estudiante(self.ui.Nombre.text(), self.ui.Correo.text(), self.ui.Contrasena.text())
        print(str(v))
        # Enviar Objeto
        msg = str(v)
        bytes = msg.encode()
        self.cliente.send(bytes)

    def abrirArchivo(self):
        filename = QFileDialog.getOpenFileName(self,'Abrir Archivo', '.', 'Text Files(**)')
        file = open(filename[0],'rb')
        self.ui.AbrirArchivo.setText(filename[0])
        count = 0
        size = 0


        print(f'Size: {size} ({size / 1024:.2f} kB)')
        i = file.read(500)

        f2 = open('copia.zip', 'wb')

        while i:
            f2.write(i)
            print(f'[{count + 1}:{len(i)}]{i}')
            count += 1
            size += len(i)
            i = file.read(500)

        f2.close()
        file.close()

    def enviarArchivo(self):

        file = open('copia.zip','rb')
        count = 0
        size = 0

        print(f'Size: {size} ({size / 1024:.2f} kB)')
        i = file.read(500)
        msg = 'iniciozip'
        bytes = msg.encode()
        self.cliente.send(bytes)
        while i:
            print(f'[{count + 1}:{len(i)}]{i}')
            pkt = i
            time.sleep(.01)
            self.cliente.send(pkt)
            count += 1
            size += len(i)
            i = file.read(500)

        msg = 'finzip'
        bytes = msg.encode()
        self.cliente.send(bytes)
        file.close()