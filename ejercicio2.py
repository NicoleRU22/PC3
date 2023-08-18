"""Cree un programa que solicite al usuario una lista de calificaciones separadas por comas. Divida
la cadena en calificaciones individuales y almacénelas en una lista para luego convertir cada
calificación en un entero. Deberá utilizar una sentencia try/except para informar al usuario
cuando los valores introducidos no puedan ser convertidos debido a un error de tipeo o
formato. (Los métodos de cadena le serán de utilidad)"""

def listadenotas():
    while True: 
        try:
            notaingresada= input("Ingrese una lista de calificaciones separadas por comas: ")
            n= notaingresada.split(',')
            lista=[]
            for notas_str in n:
                notas=int(notas_str.strip())
                lista.append(notas)
            return lista    
        except ValueError:
            print("Los valores introducidos no puedan ser convertidos debido a un error de tipeo o formato")    
lista=listadenotas()
print(f'IMPRIMIENDO NOTAS...{lista}')
