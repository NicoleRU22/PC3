"""Cree una clase Alumno e inicialícela con el nombre y el número de registro. Haga los métodos
para:
1. Display - Debe mostrar toda la información del estudiante (nombre y número de
registro).
2. setAge - Debe asignar la edad al estudiante
3. setNota - Debe asignar las notas al estudiante."""

class Alumno:
    def __init__(self, nombre, numeroregistro):
        self.nombre = nombre
        self.numeroregistro = numeroregistro
        self.notas = []

    def display(self):
        print("Mostrando información del estudiante:")
        print("Nombre:", self.nombre)
        print("Número de registro:", self.numeroregistro)
        print("Edad:", self.edad)
        print("Notas:", ", ".join(map(str, self.notas)))

    def setAge(self, edad):
        self.edad = edad

    def setNota(self, notas):
        self.notas = notas

nombre_alumno = input("Ingrese nombre del alumno: ")
numero_registro_alumno = input("Ingrese el número de registro del alumno: ")
alumno = Alumno(nombre_alumno, numero_registro_alumno)

edad_alumno = int(input("Ingrese edad del alumno: "))
alumno.setAge(edad_alumno)

notas_alumno = input("Ingrese notas del alumno separadas por (,): ").split(',')
notas_alumno = [float(nota.strip()) for nota in notas_alumno]
alumno.setNota(notas_alumno)

alumno.display()
