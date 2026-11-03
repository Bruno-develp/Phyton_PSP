import subprocess

ruta = input("Introduce la ruta de la carpeta: ")

try:
    resultado = subprocess.run(["powershell.exe", "/c", "dir"], cwd = ruta, capture_output = True, text = True, timeout = 5, check = True, encoding = "cp1252")
    
    print("El comando se realizo correctamente")
    print("Codigo de salida: ", resultado.returncode)
    print("Listado del directorio seleccionado: ", resultado.stdout)
    
except NotADirectoryError as e:
    print("La ruta o el directorio especificado no existe.", e.errno  )