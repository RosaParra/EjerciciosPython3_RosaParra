# Rosa Elizabeth Parra Sosa
# Tarea 5. Gui

from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtCore import Slot
from Estudiantes import Ui_StudentsRegister
from Tarea_MongoEngine import Estudiantes

es=Estudiantes
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_StudentsRegister()
        self.ui.setupUi(self)
        self.registros = []
        self.regcount = 0

        self.ui.Registrar.clicked.connect(self.registrar)
        self.ui.Buscar.clicked.connect(self.buscar)
        self.ui.Actualizar.clicked.connect(self.actualizar)
        self.ui.Eliminar.clicked.connect(self.eliminar)

    def registrar(self):
        self.ui.cuadro.clear()
        tmp = es.guardar(self.ui.Nombre_LEdit.text(), self.ui.Apellido_LEdit.text(),
                         self.ui.Correo_LEdit.text(), self.ui.Con_LEdit.text())

        self.registros.append(tmp)
        self.ui.cuadro.append(f'El Usuario {self.ui.Nombre_LEdit.text()} ha sido agregado '
                              f'a la base de datos, su información es la siguiente: \n \n'
                              f'{tmp}')
        self.ui.Nombre_LEdit.clear()
        self.ui.Apellido_LEdit.clear()
        self.ui.Correo_LEdit.clear()
        self.ui.Con_LEdit.clear()

    def buscar(self):
        self.ui.cuadro.clear()
        tmp = es.leer(self.ui.Referencia.text())
        self.ui.cuadro.append(f'El Usuario {self.ui.Nombre_LEdit.text()} ha sido buscado '
                              f'a la base de datos, su información es la siguiente: \n \n'
                              f'{tmp}')
        self.ui.Referencia.clear()

    def actualizar(self):
        self.ui.cuadro.clear()
        tmp = es.actualizar(self.ui.Referencia.text(), self.ui.Nombre_LEdit.text(), self.ui.Apellido_LEdit.text(),
                         self.ui.Correo_LEdit.text(), self.ui.Con_LEdit.text())
        self.ui.cuadro.append(f'El Usuario {self.ui.Nombre_LEdit.text()} ha sido actualizado '
                              f'en la base de datos, su nueva información es la siguiente: \n \n'
                              f'{tmp}')
        self.ui.Referencia.clear()
        self.ui.Nombre_LEdit.clear()
        self.ui.Apellido_LEdit.clear()
        self.ui.Correo_LEdit.clear()
        self.ui.Con_LEdit.clear()

    def eliminar(self):
        self.ui.cuadro.clear()
        tmp = es.eliminar(self.ui.Referencia.text())
        self.ui.cuadro.append(tmp)
        self.ui.Referencia.clear()
        self.mostrarTodos()

    def mostrarTodos(self):
        self.ui.cuadro.append('\n Los Estudiantes en la base de Datos son: ')
        for students in Estudiantes.objects:
            self.ui.cuadro.append(f'\n Nombre: {students.nombre}')




if __name__=='__main__':

    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec_()

