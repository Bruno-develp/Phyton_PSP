import subprocess

resultado = subprocess.run(["ipconfig"], text = True,  capture_output = True, encoding = "cp1252", shell = True)


for linea in resultado.stdout.splitlines():
    if "IPv4" in linea:
        print(linea)
