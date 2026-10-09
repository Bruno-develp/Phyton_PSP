import subprocess 
import sys 
print("1. Padre: antes de run") 
result = subprocess.run( [sys.executable, "-c", "print('hola')"] ) 
print("2. Padre: después de run")


