# Slicing
letras = ["a", "b", "c", "d", "e"]
print(letras[1:4])  # ["b", "c", "d"]
print(letras[:3])   # ?
print(letras[-2:])  # ?

cuadrados = [x**2 for x in range(6)]
print(cuadrados)  # [0, 1, 4, 9, 16]

# equivalente a
cuadrados = []
for x in range(5):
    cuadrados.append(x**2) 
print(cuadrados)  # [0, 1, 4, 9, 16]

