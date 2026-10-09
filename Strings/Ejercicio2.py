cadena = input("Introduce el texto principal: ")
subcadena = input("Introduce el texto a buscar al inicio: ")

if cadena.startswith(subcadena):
    print("Sí, la cadena comienza por esa subcadena.")
else:
    print("No, la cadena no comienza por esa subcadena.")

