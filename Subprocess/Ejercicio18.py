import subprocess

try:
    ip = input("Introduce la IP: ")
    resultado = subprocess.run(["ping", "-n", "4", ip], 
            capture_output = True, 
            text = True, 
            timeout = 10, 
            encoding = "cp1252"
            )
    
    with open("diagnostico.txt", "w", encoding = "utf-8") as fichero:
        fichero.write(resultado.stdout)
        print("Codigo salida: ", resultado.returncode)
        if resultado.returncode == 0:
            print("El comando termino correctamente")
        else:
            print("El comando termino en error")
except subprocess.TimeoutExpired:
    print("Se ha superado el tiempo maximo")
except FileNotFoundError:
    print("No se encuentra el fichero ")
    