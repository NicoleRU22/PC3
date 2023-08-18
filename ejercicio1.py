def procentaje_combustible():
    while True:
        try:
            fracciòningresada = input("Ingrese la fracción en formato X/Y: ")
            x, y = map(int, fracciòningresada.split('/'))

            if y == 0 or x < y:
                print("Error")
                continue
            porcentaje = (x / y) * 100
            if porcentaje < 1:
                result = "E"
            elif porcentaje> 99:
                result = "F"
            else:
                result = f"{round(porcentaje)}%"
            return result
        except ValueError:
            print("Error: Ingrese una nueva fracción.")
        except ZeroDivisionError:
            print("Error")

cantidad = procentaje_combustible()
print("La cantidad de combustible en el tanque es:", cantidad)
