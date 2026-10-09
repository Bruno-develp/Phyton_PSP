numeros = [1, 2, 3, 3, 1, 4]

user = int(input("Introduce un numero entre el 1 - 4: "))

con = 0

for i in range(0, len(numeros)):
    if numeros[i] == user:
        con += 1
        
print(con)        

