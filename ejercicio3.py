"""Definir una clase llamada “CIRCULO” la cual contenga un atributo inicializador radio. La clase
“CIRCULO” debe tener un método que puede calcular el área en utilizando el atributo radio."""
import math
class Circulo:
    def __init__(self, radio):
        self.radio = radio
    def calculodearea(self):
        area = math.pi * self.radio ** 2
        return area
    
radio_del_circulo = float(input("Ingrese el radio del círculo: "))
circulo = Circulo(radio_del_circulo)

area = circulo.calculodearea()
print(f"El área del círculo con radio {radio_del_circulo} es: {area}")
