"""Definir una clase llamada “RECTANGULO” que puede ser construida por los atributos largo y
ancho. La clase “RECTANGULO” debe tener un método que puede calcular el área utilizando los
atributos de la clase."""
class Rectangulo:
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho
    
    def calculodearea(self):
        area = self.largo * self.ancho
        return area

largoingresado= int(input("Ingrese largo del rectángulo: "))
anchoingresado = int(input("Ingrese ancho del rectángulo: "))
rectangulo = Rectangulo(largoingresado, anchoingresado)
area = rectangulo.calculodearea()
print(f"El área del rectángulo es: {area:.4f}")
