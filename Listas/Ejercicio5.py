numeros = [1, 2, 2, 3, 3, 4, 5]

unicos = []

for i in range(0, len(numeros)):
    if numeros[i] not in unicos:
        unicos.append(numeros[i])
        
print(unicos)




