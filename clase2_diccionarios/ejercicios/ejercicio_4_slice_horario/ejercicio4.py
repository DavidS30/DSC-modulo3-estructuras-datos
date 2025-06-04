texto = input("Digite un texto: ").lower().replace(" ","")
frecuencia = {}

for char in texto:
    frecuencia[char] = texto.count(char)

print("\nFrecuenccia de Caracteres")
for char, frecuencia in frecuencia.items():
    print(f"El caracter {char} tiene la siguiente frecuencia: {frecuencia}")