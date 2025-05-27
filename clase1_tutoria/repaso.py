# Repaso tuplas

a = 10, 20
print(type(a))

b = (10)
print(type(b))

c = (10,)
print(type(c))

# Operaciones con listas

A = [1, 2, 3]
B = ['A', 'B', 'C']
print(A+B)
print(['X', 'Y', 'Z'] * 3)

# operadores de asignacion aumentados
A = ["vaca", "perro"]
B = ["gato"]
A+=B
print(A)
bacon = ['Zophie']
bacon *= 3
print(bacon)

# repaso metodos
spam = ['a', 'z', 'A', 'Z']
spam.sort()
print(spam)
spam.sort(key=str.lower)


productos = [("cuaderno", 5000), ("lapicero", 1200), ("marcador", 3000)]
print("Original:", productos)
productos.sort(key=lambda x: x[1])
print("Ordenado por precio:", productos)
productos.sort(key=lambda x: x[0])
print("Ordenado por nombre:", productos)

# Copia
spam = [0, 1, 2, 3, 4, 5]
cheese = spam
cheese[1] = 'Hello!'
print(spam)
print(cheese)
cheese.append("World")
print(spam)


eggs = ['cat', 'dog']
print(id(eggs))
eggs.append('moose')
print(id(eggs))

eggs = ['bat', 'rat', 'cow']
print(id(eggs))


# Copia controlada
import copy
spam = ['A', 'B', 'C', 'D']
print(id(spam))
cheese = copy.copy(spam)
print(id(cheese))
cheese[1] = 42
print(spam)
