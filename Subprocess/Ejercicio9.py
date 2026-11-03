import subprocess

resultado = subprocess.run(["type", "archiuvo.txt"], capture_output = True, encoding = "cp1252", shell = True)
print("Salida estandar: ")
print(resultado.stdout)
print(resultado.stderr)