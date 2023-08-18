"""En este ejercicio vas a trabajar el concepto de puntos, coordenadas y vectores sobre el plano cartesiano y 
cómo la programación Orientada a Objetos puede ser una excelente aliada para trabajar con ellos. 
No está pensado para que hagas ningún tipo de cálculo sino para que practiques la automatización de tareas.
"""

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def mostrar_coordenadas(self):
        print(f"Las coordenadas del punto son: ({self.x}, {self.y})")
x = input("Ingrese la coordenada x: ")
y = input("Ingrese la coordenada y: ")
punto = Punto(x, y)
punto.mostrar_coordenadas()
