tareas = []

tareas.append("Hacer ejercicio")
tareas.append("Hacer el almuerzo")
tareas.append("Hacer la comida")

print("Lista de tareas:")
for tarea in tareas:
    print("- ", tarea)

tareas.remove("Hacer el almuerzo")
print(tareas)

tareas.append("Sacar a la mascota")

tareas.sort()

print(tareas)

tareas.pop()