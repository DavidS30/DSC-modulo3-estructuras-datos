myCat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}

print(myCat['size'])

print('My cat has ' + myCat['color'] + ' fur.')

spam = {12345: 'Pregunta', 42: 'Respuesta'}


## List vs Dict

spam = ['cats', 'dogs', 'moose']
bacon = ['dogs', 'moose', 'cats']

print(spam == bacon) # ?

eggs = {'name': 'Zophie', 'species': 'cat', 'age': '8'}
ham = {'species': 'cat', 'age': '8', 'name': 'Zophie'}
print(eggs == ham) # ?

## key Error

spam = {'name': 'Zophie', 'age': 7}
print(spam['color']) # ?

## Orden en dicts

eggs = {'name': 'Zophie', 'species': 'cat', 'age': '8'}
list(eggs)

ham = {'species': 'cat', 'age': '8', 'name': 'Zophie'}
list(ham)

spam = {}
spam['first key'] = 'value'
spam['second key'] = 'value'
spam['third key'] = 'value'
list(spam)

# Recorrido

spam = {'color': 'red', 'age': 42}

for v in spam.values():
    print(v)

for k in spam.keys():
    print(k)

for i in spam.items():
    print(i)


for k, v in spam.items():
    print('Key: ' + k + ' Value: ' + str(v))

# Existencia en diccionarios
spam = {'name': 'Zophie', 'age': 7}
'name' in spam.keys()

'Zophie' in spam.values()

'color' in spam.keys()

'color' not in spam.keys()

'color' in spam

# Metodos

picnicItems = {'apples': 5, 'cups': 2}

'I am bringing ' + str(picnicItems.get('cups', 0)) + ' cups.'

'I am bringing ' + str(picnicItems.get('eggs', 0)) + ' eggs.'
#'I am bringing ' + str(picnicItems['eggs']) + ' eggs.'

## Valores por defecto

spam = {'name': 'Pooka', 'age': 5}
if 'color' not in spam:
    spam['color'] = 'black'


spam = {'name': 'Pooka', 'age': 5}
spam.setdefault('color', 'black')
spam.setdefault('color', 'white') # ?

spam