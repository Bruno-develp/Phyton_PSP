calificaciones = {}

num_estudiantes = int(input("¿Cuántos estudiantes quieres agregar?: "))

for i in range(num_estudiantes):
    nombre = input(f"Introduce el nombre del estudiante {i + 1}: ")
    calificacion = int(input(f"Introduce la calificación de {nombre}: "))
    calificaciones[nombre] = calificacion

print("Diccionario de estudiantes y calificaciones:", calificaciones)
