#''
#Desafío de listas dinámicas:
# ingresar N productos y generar un reporte limpio.
#''

productos = []

while True:
    try:
        cantidad = int(input("¿Cuántos productos quieres ingresar? "))
        if cantidad <= 0:
            print("Por favor, ingresa un número mayor a cero.")
            continue
        break
    except ValueError:
        print("Por favor, ingresa un número entero válido.")

for i in range(cantidad):
    nombre = input(f"Ingrese por favor el producto {i+1}: ")
    while True:
        try:
            precio = float(input("Ingrese el precio del producto digitado: "))
            if precio < 0:
                print("El precio no puede ser negativo. Intenta de nuevo.")
                continue
            break
        except ValueError:
            print("Por favor, ingresa un precio válido (número).")
    productos.append([nombre, precio])

def imprimir_reporte_productos(lista_productos):
    print("\n\nReporte de Productos: ")
    lista_productos.sort(key=lambda producto: producto[1])
    for prod in lista_productos:
        print(f"- {prod[0]} con precio: {prod[1]}")

imprimir_reporte_productos(productos)