numeros = [4, 10, 5, 2]

mayor = numeros[0]

for numero in numeros:
    if numero > mayor:
        mayor = numero

print(f"El numero mas grande es: {mayor}")