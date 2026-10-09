lista = ["a", "b", "c", "d", "e"]

vocales = 0

for letra in lista:
    if letra in ("aeiou"):
        vocales += 1

print(vocales)