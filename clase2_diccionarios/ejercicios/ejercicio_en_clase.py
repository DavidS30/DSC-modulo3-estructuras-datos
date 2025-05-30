# Debemos instanciar un diccionario de inventario
# Con un while true y con inputs debemos solicitar: Producto y cantidad
# El producto debe ser la llave y la cantidad el valor
# Despues de ingresar los productos tendremos la opción de salir y
# finalmente imprimimos el reporte de productos de esta forma:
# EJem: Producto: Manzana, Cantidad: 5

inventario = {}

while True:
    producto = input("Digite el nombre del producto ( 0 digite salir para generar reporte): ")
    if producto.lower() == 'salir':
        break
    if not producto.strip():
        print("El nombre del producto no puede estar vacío. Intente de nuevo.")
        continue
    while True:
        try:
            cantidad = int(input(f"Digite la cantidad del producto {producto}: "))
            if cantidad < 0:
                print("La cantidad no puede ser negativa. Intente de nuevo.")
                continue
            break
        except ValueError:
            print("Por favor, ingrese un número entero válido para la cantidad.")
    inventario[producto] = inventario.get(producto, 0) + cantidad

print("\n Reporte de inventario:")
for prod,cant in inventario.items():
    print(f"- Producto: {prod}, Cantidad: {cant}")

