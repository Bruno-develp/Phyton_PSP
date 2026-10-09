import subprocess

termino = input("Introduce el término que quieres buscar en Google: ")

url = f"https://www.google.com/search?q={termino}"

subprocess.run(f"START {url}", shell=True)


