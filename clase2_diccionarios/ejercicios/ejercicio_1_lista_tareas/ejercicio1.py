frase = input("Digite una frase: ") # hola mundo como estas
palabras = frase.split()
conteo = {}

for palabra in palabras:
    palabra = palabra.lower()
    conteo[palabra] = palabras.count(palabra)

print("Conteo de palabras: ", conteo)

