
def ingresar_productos(proveedor):
    print(f"\n===* Ingreso de productos {proveedor} *===")
    productos = []

    while True:
        try:
            nombre_producto = input("Escriba el nombre del producto (o 'fin' para salir): ")
            if nombre_producto.lower() == 'fin':
                break
            stock = int(input(f"Ingrese el stock para {nombre_producto}: "))
            if stock < 0:
                print("La cantidad del stock no puede ser negativa.")
                continue
            productos.append({'nombre': nombre_producto, 'stock': stock})
        except ValueError:
            print("Por favor, ingrese un número entero valido para el stock.")
    return  productos

# Llenar data
productos_m = ingresar_productos("Microsoft")
productos_n = ingresar_productos("Nvidia")

# Construir conjuntos
nombres_m = {producto["nombre"] for producto in productos_m}
nombres_n = {producto["nombre"] for producto in productos_n}

#Mostrar los conjuntos
print(f"\nProductos únicos en proveedor Microsoft: {nombres_m}")
print(f"Productos únicos en proveedor Nvidia: {nombres_n}")

#Productos en comunes en ambos proveedores
comunes = nombres_m & nombres_n
print("Productos que estan en ambos proveedores:", comunes)

#Productos únicos en total de los proveedores
unicos = nombres_m ^ nombres_n
print("Productos únicos de los proveedores:", unicos)

inventario_total = {}
for producto in productos_m + productos_n:
    nombre = producto["nombre"]
    stock = producto["stock"]
    inventario_total[nombre] = inventario_total.get(nombre, 0) + stock

print("\n===* Inventario Consolidado *===")
for nombre,stock in inventario_total.items():
    print(f"- {nombre}: {stock} unidades")

# Validación -> Me avise si algun producto tiene menos de una cantidad especifica que yo pueda parametrizar.
# - Teclado: 15 unidades
# - Mouse: 2 unidades
# - Tarjeta: 10 unidades

# El producto Mouse tiene bajo stock
STOCK_MINIMO = 5
print("===* Validación de bajo stock ( minimo 5 unidades ) *===")
for nombre,stock in inventario_total.items():
    if stock < STOCK_MINIMO:
        print(f"El producto {nombre} tiene bajo stock ({stock} unidades)")
