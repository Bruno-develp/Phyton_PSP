import subprocess

try:
    subprocess.run(["dir"], check=True, shell=True)
    print("El comando se ejecutó correctamente.")

except subprocess.CalledProcessError as error:
    print("El proceso terminó con error (código distinto de cero).")
    print("Código:", error.returncode)

except FileNotFoundError as error:
    print("El archivo o ejecutable no existe en el sistema.")
    print("Detalle:", error)