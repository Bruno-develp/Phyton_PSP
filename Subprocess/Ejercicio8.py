import subprocess

resultado = subprocess.run(["ipconfig"])
print(resultado.returncode)

if resultado.returncode == 0:
    print("El programa termino correctamente")
else:
    print("El programa no termino correctamente")

