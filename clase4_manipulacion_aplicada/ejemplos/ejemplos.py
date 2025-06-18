
# ===* Funciones Lambda *===
# Función tradicional
def cuadrado(x):
    return x**2
cuadrado(2)
# Función lambda equivalente
#lambda argument(s) : expression
cuadrado = lambda x: x**2
print(cuadrado(4))

# invocar lambda directamente
(lambda x: x*2)(6)

# mas argumentos
suma = lambda x,y: x+y
multiplica = lambda x,y: x*y

suma(3,4)
multiplica(2,6)

#ejercicio: crea una función lambda que elimine los duplicados de dos listas
# y devuelva un cojunto con la unión de ambas listas sin duplicados.

elimina_duplicados = lambda x,y: set(x) | set(y)

elimina_duplicados([1,2,2,2,3,3,4,5], [5,6,6,7,7,7,8,9])
#{1,2,3,4,5,6,7,8,9}
# ===* Operaciones con MAP *===

# Lista de números
numeros = [1, 2, 3, 4, 5]

# sintaxis: map(func, iter)
cuadrados = list(map(lambda x: x * x, numeros))
print(f"Cuadrados: {cuadrados}")

# Lista de palabras
palabras = ["hola", "mundo", "python", "lambda"]

mayusculas = list(map(lambda s: s.upper(), palabras))
print(f"Mayúsculas: {mayusculas}")

# Trabajar con diccionarios
usuarios = [
    {"nombre": "Alice", "edad": 30},
    {"nombre": "Bob", "edad": 24},
    {"nombre": "Charlie", "edad": 35}
]

nombres = list(map(lambda u: u["nombre"], usuarios))
print(f"Nombres de usuarios: {nombres}")

# Incrementar la edad de cada usuario en 1 año
usuarios_nuevas_edades = list(map(lambda u: {"nombre": u["nombre"], "edad": u["edad"] + 1}, usuarios))
print(f"Usuarios con edades incrementadas: {usuarios_nuevas_edades}")

#===* operaciones con filter *===
# Lista de números
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Filtrar números pares usando filter y lambda
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(f"Números pares: {pares}")

# Filtrar números mayores que 5
mayores_que_cinco = list(filter(lambda x: x > 5, numeros))
print(f"Números mayores que 5: {mayores_que_cinco}")

# Lista de productos con diccionarios
productos = [
    {"nombre": "Laptop", "precio": 1200, "stock": 5},
    {"nombre": "Teclado", "precio": 75, "stock": 12},
    {"nombre": "Mouse", "precio": 25, "stock": 0},
    {"nombre": "Monitor", "precio": 300, "stock": 8}
]

# Filtrar productos con stock disponible
productos_disponibles = list(filter(lambda p: p["stock"] > 0, productos))
print(f"Productos disponibles: {productos_disponibles}")

# Filtrar productos con precio mayor a 100
productos_caros = list(filter(lambda p: p["precio"] > 100, productos))
productos_caros_nombre = list(map(lambda p: p["nombre"], productos_caros))
print(f"Productos caros: {productos_caros_nombre}")

#===* OPERACIONES CON REDUCE *===
from functools import reduce

# Lista de números
numeros = [10, 2, 3, 4, 5]

# Sumar todos los números usando reduce y lambda
suma_total = reduce(lambda x, y: x + y, numeros)
print(f"Suma total: {suma_total}")

# Multiplicar todos los números
producto_total = reduce(lambda x, y: x * y, numeros)
print(f"Producto total: {producto_total}")

# Encontrar el número más grande en una lista
el_mas_grande = reduce(lambda x, y: x if x > y else y, numeros)
print(f"El número más grande: {el_mas_grande}")

# Concatenar cadenas
palabras = ["Esto", "es", "una", "prueba"]
frase = reduce(lambda acc, word: acc + " " + word, palabras)
print(f"Frase concatenada: {frase}")

# Reduce con diccionarios
ventas_diarias = [
    {"fecha": "2023-01-01", "monto": 100},
    {"fecha": "2023-01-02", "monto": 150},
    {"fecha": "2023-01-03", "monto": 75}
]

# Calcular el monto total de ventas
total_ventas = reduce(lambda acc, venta: acc + venta["monto"], ventas_diarias, 0)
print(f"Total de ventas: ${total_ventas}")


# ===* Validación de datos antes de ingresar *===
# Datos con posibles errores
usuarios_crudos = [
    {"id": 1, "nombre": "Alice", "email": "alice@example.com", "edad": 30},
    {"id": 2, "nombre": "", "email": "bob@example.com", "edad": 22}, # Nombre vacío
    {"id": 3, "nombre": "Charlie", "email": "charlie@.com", "edad": 45}, # Email inválido
    {"id": 4, "nombre": "David", "email": "david@example.com", "edad": -5}, # Edad inválida
    {"id": 5, "nombre": "Eve", "email": "eve@example.com", "edad": None} # Edad nula
]

# Funciones de validación usando lambdas

es_nombre_valido = lambda u: isinstance(u.get("nombre"), str) and len(u["nombre"].strip()) > 0
es_email_valido = lambda u: isinstance(u.get("email"), str) and "@" in u["email"] and "." in u["email"].split("@")[-1]
es_edad_valida = lambda u: isinstance(u.get("edad"), int) and u["edad"] > 0

# Combinar las validaciones usando filter
usuarios_validos = list(filter(lambda u: es_nombre_valido(u) and es_email_valido(u) and es_edad_valida(u), usuarios_crudos))

print("===* Validación de Datos *===")
print(f"Usuarios crudos: {usuarios_crudos}")
print(f"Usuarios válidos después de filtrar: {usuarios_validos}")

## Ejercicio: dado un listado de strings con numeros, filtrar únicamente si
#son números flotantes validos.
precios_str = ["10.50", "20", "30.75", "no-es-un-numero", "1a2-21", "123.21"]

def es_valido_flotante(strp):
    try:
        float(strp)
        return True
    except ValueError:
        return False

precios_validos = list(filter(lambda x: es_valido_flotante(x), precios_str))
precios_validos_convertidos = list(map(lambda x: float(x), precios_validos))
print("Precios: ", precios_validos_convertidos)
# filter(func, lista) -> func tiene que devolver o true o false, si es true pasa, sino no pasa.


# Trabajemos con JSON
import json

# Simulación de datos JSON recibidos (como una cadena)
json_data_str = """
[
    {"id": "usr_001", "name": "Carlos", "email": "carlos@example.com", "isActive": true, "roles": ["admin", "editor"]},
    {"id": "usr_002", "name": "Maria", "email": "maria@example.com", "isActive": false, "roles": ["viewer"]},
    {"id": "usr_003", "name": "Pedro", "email": "pedro@example.com", "isActive": true, "roles": ["editor"]},
    {"id": "usr_004", "name": "Lucia", "email": "lucia@example.com", "isActive": true, "roles": ["admin", "viewer"]},
    {"id": "usr_005", "name": "Jorge", "email": "jorge@example.com", "isActive": false, "roles": ["editor", "viewer"]},
    {"id": "usr_006", "name": "Ana", "email": "ana@example.com", "isActive": true, "roles": ["editor", "admin", "viewer"]},
    {"id": "usr_007", "name": "Sofia", "email": "sofia@example.com", "isActive": false, "roles": ["viewer"]},
    {"id": "usr_008", "name": "Miguel", "email": "miguel@example.com", "isActive": true, "roles": []}
]
"""

# Cargar los datos JSON en una estructura Python
usuarios_json = json.loads(json_data_str)

print("--- Procesamiento de Datos JSON ---")
print(f"Datos JSON cargados: {usuarios_json}")

# Filtrar usuarios activos
usuarios_activos = list(filter(lambda u: u["isActive"], usuarios_json))
usuarios_activos_nombres = list(map(lambda u: u['name'], usuarios_activos))
print(f"Usuarios activos: {usuarios_activos_nombres}")

# Extraer solo el id y el nombre de cada usuario
info_usuarios = list(map(lambda u: {"id": u["id"], "nombre": u["name"]}, usuarios_json))
print(f"Información simplificada de usuarios: {info_usuarios}")

# Determinar si todos los usuarios tienen al menos un rol
todos_tienen_rol = all(map(lambda u: len(u["roles"]) > 0, usuarios_json))
print(f"¿Todos los usuarios tienen al menos un rol? {todos_tienen_rol}")

# Crear una lista de emails de usuarios con rol "admin"
emails_admin = list(filter(lambda u: "admin" in u["roles"], usuarios_json))
emails_admin_list = list(map(lambda u: u["email"], emails_admin))
print(f"Emails de administradores: {emails_admin_list}")

# Obtener una lista de todos los roles de todos los usuarios
todos_los_roles = reduce(lambda acc, user: acc + user["roles"], usuarios_json, [])
sin_duplicados = set(todos_los_roles)
print(sin_duplicados)
print("===* Mis roles actuales *===")
for v in sin_duplicados:
    print(v + "\n")

# Ejercicio Encontrar un usuario específico por email
# Quiero que busquen este email: david@mail.com

email_a_buscar = "sofia2@example.com"
usuario_filtrado = list(filter(lambda usuario: usuario['email'] == email_a_buscar, usuarios_json))
if usuario_filtrado:
    print("usuario filtrado: ", usuario_filtrado)
else:
    print("No encontramos usuario")
