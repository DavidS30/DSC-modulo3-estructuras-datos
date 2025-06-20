
#Definición de conjuntos
libros = set()
autores = set()
prestamos = set() # {("NombreLibro", "David", "01-01-2025"), ("NombreLibro", "David", "01-01-2025"), ("NombreLibro", "David", "01-01-2025")}
usuarios = set() # {"David", "Jorge", "Giovanni"}

# Ingreso libros y los autores
print("===* Registro de libros y autores *===")
while True:
    nombre_libro = input("Nombre del libro (o 'fin' para terminar): ").strip()
    if nombre_libro == '':
        print("El nombre del libro no puede estar vacio. Por favor vuelva a diligenciar.")
        continue
    if nombre_libro.lower() == 'fin':
        break
    nombre_autor = input(f"Ingrese el autor del libro {nombre_libro}: ").strip()
    if nombre_autor == '':
        print("El nombre del autor no puede estar vacio. Por favor vuelva a diligenciar.")
        continue
    libros.add(nombre_libro)
    autores.add(nombre_autor)

# Ingreso del usuarios
print("===* Registro de Usuarios *===")
while True:
    nombre_usuario = input("Nombre del usuario (o 'fin' para terminar): ").strip()
    if nombre_usuario == '':
        print("El nombre del usuario no puede estar vacio. Por favor vuelva a diligenciar.")
        continue
    if nombre_usuario.lower() == 'fin':
        break
    usuarios.add(nombre_usuario)

# Ingreso de prestamos
print("===* Registro de Prestamos *===")
while True:
    libro = input("Libro a prestar (o 'fin' para terminar): ").strip()
    if libro == '':
        print("El nombre del libro no puede estar vacio. Por favor vuelva a diligenciar.")
        continue
    if libro.lower() == 'fin':
        break
    usuario = input("Digite el usuario que tomará el prestamo: ").strip()
    fecha = input("Digite la fecha del préstamo: (DD-MM-YYYY): ").strip()
    if libro in libros and usuario in usuarios:
        prestamos.add((libro,usuario,fecha))
    else:
        print("Libro o usuario no encontrado o registrado. Valide por favor")

# Lógica de presentación | Informe y datos

print("\n===* Informe general de la Biblioteca *===")
print("Libros registrados: ", libros)
print("Autores registrados: ", autores)
print("Usuarios registrados: ", usuarios)
print("Prestamos registrados: ", prestamos)

# Operaciones con conjuntos
libros_prestados = {p[0] for p in prestamos}
usuarios_con_prestamo = {p[1] for p in prestamos}
print("\nLibros prestados: ", libros_prestados)
print("\nLibros NO prestados: ", libros - libros_prestados)
print("\nUsuarios con prestamo: ", usuarios_con_prestamo)
print("\nUsuarios sin prestados: ", usuarios - usuarios_con_prestamo)

print("\n===* Comparaciones *===")

if libros_prestados.issubset(libros):
    print("Todos los libros prestados pertenecen a la biblioteca (issubset).")
if libros.issuperset(libros_prestados):
    print("La biblioteca contiene todos los libros prestados (issuperset).")
if usuarios.isdisjoint(autores):
    print("No hay usuarios que sean autores de los libros (isdisjoint).")
else:
    print("Tenemos usuarios que son autores de libros.")