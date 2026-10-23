import subprocess

resultado = subprocess.run(["taskList"], capture_output = True, text = True, encoding = "cp1252")
 
print(resultado.stdout)

lineas = resultado.stdout.splitlines()

print(lineas)

print ("-------------------------------------------------")

for linea in lineas: 
    if "python" in linea: 
        print(linea)


