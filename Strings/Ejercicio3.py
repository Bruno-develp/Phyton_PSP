cadena = input("Introduce una cadena: ")
caracter = input("Introduce un caracter: ")

if caracter.isalpha():
    print(cadena.count(caracter, 0, len(cadena)))
else:
    print("El elemento introducido no es un caracter")