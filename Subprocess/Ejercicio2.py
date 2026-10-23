import subprocess

resultado = subprocess.run(["ipconfig"], capture_output = True, encoding = "cp1252", shell = True)
print(resultado.stdout)