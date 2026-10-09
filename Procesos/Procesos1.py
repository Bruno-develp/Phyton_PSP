import subprocess

#fichero = open("fichero.txt", 'w')
#fichero.write("Este es mi fichero creado desde Phyton")
#fichero.close()

with open("fichero.txt", 'w') as fichero:
    fichero.write("Este es mi fichero creado desde Python")

subprocess.run(["notepad.exe", "fichero.txt"],
               shell = True)
