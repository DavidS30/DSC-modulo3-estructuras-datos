# --- Lectura de Archivos ---

# Primero, creamos un archivo de ejemplo para leer
with open("ejemplo.txt", "w") as archivo:
    archivo.write("Hola, este es un archivo de texto.\n")
    archivo.write("Contiene varias líneas de contenido.\n")
    archivo.write("Vamos a leerlo y procesarlo.\n")

print("--- Leyendo el archivo completo ---")
try:
    with open("ejemplo.txt", "r") as archivo:
        contenido = archivo.read() # Lee todo el contenido del archivo como una sola cadena
        print(contenido)
except FileNotFoundError:
    print("Error: El archivo 'ejemplo.txt' no se encontró.")
except Exception as e:
    print(f"Ocurrió un error inesperado al leer: {e}")

print("\n--- Leyendo el archivo línea por línea ---")
try:
    with open("ejemplo.txt", "r") as archivo:
        for linea in archivo: # Itera sobre el archivo, leyendo una línea a la vez
            print(f"Línea leída: {linea.strip()}") # .strip() elimina saltos de línea y espacios en blanco
except FileNotFoundError:
    print("Error: El archivo 'ejemplo.txt' no se encontró.")

print("\n--- Leyendo todas las líneas en una lista ---")
try:
    with open("ejemplo.txt", "r") as archivo:
        lineas = archivo.readlines() # Lee todas las líneas y las devuelve como una lista de cadenas
        print(f"Líneas como lista: {lineas}")
        for i, linea in enumerate(lineas):
            print(f"Línea {i+1}: {linea.strip()}")
except FileNotFoundError:
    print("Error: El archivo 'ejemplo.txt' no se encontró.")


# lectura y actualización de json
import json

# --- Persistencia con JSON ---

datos = {
    "nombre": "Alice",
    "edad": 30,
    "ciudades_visitadas": ["Bogota", "Medellin", "Cali"],
    "es_estudiante": True
}

# Guardar datos en un archivo JSON
print("\n--- Guardando datos en JSON ---")
try:
    with open("datos.json", "w") as archivo_json:
        json.dump(datos, archivo_json, indent=4) # indent para formato legible
    print("Datos guardados en 'datos.json'.")

    # Leer datos de un archivo JSON
    print("\n--- Leyendo datos desde JSON ---")
    with open("datos.json", "r") as archivo_json:
        datos_cargados = json.load(archivo_json)
        print(f"Datos cargados: {datos_cargados}")
        print(f"Tipo de datos cargados: {type(datos_cargados)}")
except Exception as e:
    print(f"Ocurrió un error al manejar JSON: {e}")