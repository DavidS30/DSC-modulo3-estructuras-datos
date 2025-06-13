# Slicing
letras = ["a", "b", "c", "d", "e"]
print(letras[1:4])  # ["b", "c", "d"]
print(letras[:3])   # ?
print(letras[-2:])  # ?

lista = range(6)
lista
#[0,1,2,3,4,5]
#[0,1,4,9,16,25]
cuadrados_list = [x**2 for x in lista]
cuadrados_list
cuadrados = [x**2 for x in range(6)]
print(cuadrados)  # [0, 1, 4, 9, 16]

# equivalente a
cuadrados = []
for x in range(5):
    cuadrados.append(x**2)
print(cuadrados)  # [0, 1, 4, 9, 16]

