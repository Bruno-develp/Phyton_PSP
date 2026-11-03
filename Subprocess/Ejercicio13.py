import subprocess

ip = input("Introduce una dirección IP o dominio: ".strip())

try:

    resultado = subprocess.run(
        ["ping", "-n", "4", ip], capture_output = True, text = True, timeout = 5, check = True, encoding = "cp1252"
    )
    
    print("Código de salida:", resultado.returncode)
    
    if resultado.returncode == 0:
        print("El proceso se realizo correctamente")
    else:
        print("El proceso termino con error")

except subprocess.TimeoutExpired:
    print("El proceso superó el tiempo de espera (timeout).")
else:
    print(resultado.stdout)



