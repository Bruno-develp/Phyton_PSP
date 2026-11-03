import subprocess

res = subprocess.run(["ipconfig", ">", "configuracion.txt"],  shell = True)
    
