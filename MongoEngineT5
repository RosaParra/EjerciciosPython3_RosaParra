# Rosa Elizabeth Parra Sosa
# Tarea 5. Base de Datos de MongoEngine actualizada

from mongoengine import *

#  Base de Datos nombre PADTS
connect('PADTS')


# Colección Estudiantes
class Estudiantes(Document):
    nombre = StringField(required=True)
    apellido = StringField(required=True)
    correo = StringField(required=True)
    contrasena = StringField(required=True)

    def guardar( nom, ap, coEl, con):
        toSave = Estudiantes(
            nombre=nom,
            apellido=ap,
            correo=coEl,
            contrasena=con
        )
        toSave.save()
        guardado = Estudiantes.leer(nom)
        return guardado

    def leer(par):
        for students in Estudiantes.objects:
            if par == students.nombre:
                leeeO =(f' Nombre: {students.nombre}\n'
                      f' Apellido: {students.apellido}\n'
                      f' Correo: {students.correo}\n'
                      f' Contraseña: {students.contrasena}')
                return leeeO

        return 'Estudiante no registrado'

    def actualizar(par, nom, ap, coEl, con):
        for students in Estudiantes.objects:
            if par == students.nombre:
                students.nombre = nom
                students.apellido = ap
                students.correo = coEl
                students.contrasena = con
                students.save()
                act =(f' Nombre: {students.nombre}\n'
                      f' Apellido: {students.apellido}\n'
                      f' Correo: {students.correo}\n'
                      f' Contraseña: {students.contrasena}')
                return act
        return 'Estudiante no registrado'
    def eliminar(par):
        for students in Estudiantes.objects:
            if par == students.nombre:
                ID=students.id
                Estudiantes.objects(id=ID).delete()
                return f'El estudiante {par} ha sido eliminado exitosamente'

        return f'El estudiante {par} no ha sido encontrado'

#
# nombres = ['Rosa', 'Elizabeth', 'Fabian', 'Alejandro', 'Rosario']
# apellidos = ['Parra', 'Sosa', 'Vazquez', 'Chavez', 'Hernandez']
# correos = ['eli.parra.ep4@gmail.com', 'rosa.parra@alumnos.udg.mx',
#            'fabian.fast@hotmail.com', 'alejandro.chavez@alumnos.udg.mx',
#            'rosario.hernandez@alumnos.udg.mx']
# contrasenas = ['abc123', 'def456', 'ghi789', 'jkl741', 'mno852']
#
es = Estudiantes
#
# # Guardar
# for n, a, ce, c in zip(nombres, apellidos, correos, contrasenas):
#     es.guardar(n, a, ce, c)
