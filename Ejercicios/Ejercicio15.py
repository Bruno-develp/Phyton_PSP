def obtener_dia(numero):
    if numero == 1:
        return "Lunes"
    elif numero == 2:
        return "Martes"
    elif numero == 3:
        return "Miércoles"
    elif numero == 4:
        return "Jueves"
    elif numero == 5:
        return "Viernes"
    elif numero == 6:
        return "Sábado"
    elif numero == 7:
        return "Domingo"
    else:
        return "Error: El número debe estar entre 1 y 7"

numero = int(input("Introduce un número del 1 al 7: "))
print(obtener_dia(numero))