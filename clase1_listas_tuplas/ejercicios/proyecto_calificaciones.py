PERFORMANCE = ["Excelente 🥳", "Bien 🫡", "Regular 😥", "Insuficiente 😞"]
def get_student_data():
    students = []
    grades = []

    print("=====* Proyecto de calificaciones *=====\n")

    while True:
        name = input("Ingrese el nombre del estudiante (o 'salir' para terminar): ").strip()
        if name.lower() == 'salir':
            break

        while True:
            try:
                grade = float(input(f"Ingrese la nota de {name} (0 - 5): "))
                if 0 <= grade <= 5:
                    break
                else:
                    print("La nota debe estar entre 0 y 5. Intenta de nuevo.")
            except ValueError:
                print("Entrada inválida. Por favor ingresa un número.")

        students.append(name)
        grades.append(grade)

        print(f"Nota de {name} registrada\n")

    return students, grades


def calculate_average(grades):
    if len(grades) == 0:
        return 0
    return sum(grades) / len(grades)


def classify_performance(grade):
    if grade >= 4.5:
        return PERFORMANCE[0]
    elif grade >= 3.5:
        return PERFORMANCE[1]
    elif grade >= 2.5:
        return PERFORMANCE[2]
    else:
        return PERFORMANCE[3]


def print_report(students, grades):
    print("\n*=== Reporte de Calificaciones ===*\n")
    for i in range(len(students)):
        classification = classify_performance(grades[i])
        print(f"{students[i]}: Nota: {grades[i]:.2f} → Rendimiento: {classification}")

    average = calculate_average(grades)
    print(f"\n*=== Promedio general del grupo: {average:.2f} ===*\n")

    print("\n*=== Fin del programa ===*\n")


def main():
    students, grades = get_student_data()

    if len(students) == 0:
        print("No se ingresaron estudiantes. Programa finalizado.")
        return

    print_report(students, grades)


if __name__ == "__main__":
    main()
