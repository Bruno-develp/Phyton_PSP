import subprocess
import time
proceso = subprocess.Popen(["ping", "-n", "4", "8.8.8.8"])
for i in range(5):
    print("El padre está trabajando...")
    time.sleep(1)



