import subprocess

nombre_carpeta = input("Introduce el nombre de la carpeta: ")
directorio = input("Introduce la ruta del directorio donde crearla (ej. C:/Users/TuUsuario/Desktop): ")

ruta_completa = f"{directorio}/{nombre_carpeta}"

subprocess.run(f"mkdir \"{ruta_completa}\"", shell=True)

subprocess.run(["explorer.exe", ruta_completa])

print("El Explorador de archivos se ha cerrado. Fin del programa.")



