frutas_colores = {
    "manzana": "rojo",
    "platano": "amarillo",
    "pera": "verde",
    "naranja": "naranja"
    }

fruta = input("Introduce fruta: ")

if fruta in frutas_colores:
    print(f"El color de la fruta {fruta} es: {frutas_colores[fruta]}")
else:
    print("Esta fruta no esta disponible")
