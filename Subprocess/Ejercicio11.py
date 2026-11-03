import subprocess

try:

    resultado = subprocess.run(
        ["ping", "127.0.0.1", "-n", "20"],
        capture_output=True,
        text=True,
        encoding="cp1252",
        timeout=10
    )
    
    print("--------- SALIDA DEL PING ------------")
    print(resultado.stdout)

except subprocess.TimeoutExpired:
    print("La operación ha tardado demasiado (se superó el límite de 3 segundos).")
