# Listas de listas
carrito = [
    ["Minecraft", 25.0, 1],
    ["FIFA 23", 60.0, 2],
    ["Among Us", 5.0, 3]
]

print("🛒 Carrito de compras:")
total = 0

for item in carrito:
    nombre = item[0]
    precio = item[1]
    cantidad = item[2]
    subtotal = precio * cantidad
    total += subtotal

    print(f"{nombre} x{cantidad} → ${subtotal:.2f}")

print(f"\n💰 Total a pagar: ${total:.2f}")

# Listas de tuplas

nevera = [
    ("Coca-Cola", 4),
    ("Agua", 3),
    ("Jugo de mora", 5),
    ("Gatorade", 6)
]

print("🧊 Estado de la nevera:")
for bebida in nevera:
    nombre, temp = bebida
    estado = "fría" if temp <= 4 else "fresca"
    print(f"{nombre}: {temp}°C → {estado}")