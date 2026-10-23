import subprocess

equipo = input("Introduce una IP de equipo: ")
subprocess.run(["ping", equipo])
