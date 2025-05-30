# *======= Ejemplo con listas =======*

productos = ["cuaderno", "lápiz", "borrador"]


# Agrega un producto al final
productos.append("regla")
print(productos)

# Inserta un producto en la posición 1
productos.insert(3, "tablero")
print(productos)

# Elimina la primera aparición de "lápiz"
productos.remove("tablero")
print(productos)

# Elimina el producto en la posición 2
eliminado = productos.pop(2)
print(eliminado)
print(productos)

# Ordena la lista alfabéticamente
productos.sort(reverse=True)
print(productos)

# Invierte el orden
productos.reverse()
print(productos)

# Longitud de la lista
print(len(productos))
productos.append("borrador")
print(productos.count("borrador"))

productos2 = ["computadora", "mouse", "teclado"]
productos.extend(productos2)

print(productos)
print("lápiz" in productos)
print("cuaderno" in productos)

# Convertir lista a cadena
cadena = ", ".join(productos)
print(cadena)

# Convertir cadena a lista
lista = cadena.split(", ")
print(lista)

productos.clear()
print(productos)



# *======= Ejemplo con tuplas =======*

# Definición de una tupla
coordenadas = (10, 20, 30)
coordenadas.reverse()
print(coordenadas)
# Acceso a elementos
print(coordenadas[0])
print(coordenadas[1])
print(coordenadas[2])

persona = ("Ana", 30, "México")
print(persona)

# Desempaquetado de tupla
nombre, edad, pais = persona
print(nombre)
print(edad)
print(pais)

# Longitud de la tupla
print(len(coordenadas))  # 2

print(10 in coordenadas)
print(50 in coordenadas)

# Tupla anidada
punto3d = (5, 10, (15, 20))
print(punto3d[2][0])
