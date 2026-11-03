import subprocess

resultado = subprocess.run(["ipconfig"], capture_output = True, encoding = "cp1252", shell = True)
print("--------- CON TEXT ------------")
print(resultado.stdout)

resultado = subprocess.run(["ipconfig"], capture_output = True)
print("--------- SIN TEXT ------------")
print(resultado.stdout)
