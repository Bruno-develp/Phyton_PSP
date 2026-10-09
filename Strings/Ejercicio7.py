def caracter(mensaje):
    while True:
        entrada = input(mensaje)
        if len(entrada) == 1:
            return entrada
        print("Error")

cadena = input("Introduce un String: ")
origen = caracter("Introduce el caracter que quieres sustituir: ")
final = caracter("Introduce caracter nuevo: ")

resultado= cadena.replace(origen, final)

print(f"El resultado es: {resultado}")