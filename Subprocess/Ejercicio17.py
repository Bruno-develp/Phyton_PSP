import subprocess

busqueda = input("Introduce un termido de busqueda: ")
url = "https://www.google.com/search?q=" + busqueda

resultado = subprocess.run(["cmd", "/c", "start", "", url])

print("Proceso padre terminado")
