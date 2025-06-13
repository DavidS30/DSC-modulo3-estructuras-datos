numbers = [1, 2, 2, 2, 3, 4, 5, 5]
set(numbers)

hex_colors = {"#33FF57"}

hex_colors = {
     "#33FF57",  # Green
     "#3357FF",  # Blue
     "#F1C40F",  # Yellow
     "#E74C3C",  # Red
 }


# Tipos diferentes
{42, "Hi!", 3.14159, None, "Python"}

#Conjuntos con tuplas o ¿listas?
rgb_colors = {
   (51, 255, 87),  # Green
   (51, 87, 255),  # Blue
   (241, 196, 15),  # Yellow
   (231, 76, 60),  # Red
 }

rgb_colors = {
     [51, 255, 87],  # Green
     [51, 87, 255],  # Blue
     [241, 196, 15],  # Yellow
     [231, 76, 60],  # Red
 }

students = {
    ("Jane", 18, ["Matematicas", "Fisica", "Historia"]),
    ("John", 19, ["Ingles", "Historia", "Filosofia"]),
}

#Instancia
empty = set()
empty
iterable = set([1, 2, 2, 3, 4, 4, 5])
iterable

language = "Python"
set(language)

set("Hello!")
{"Hello!"}

#Comprenhension de conjuntos
# Sintaxis: {expression for member in iterable [if condition]}
usernames = [
     "Alice",
     " bob",
     "ALICE  ",
     "Bob",
     "charlie",
     "Charlie",
     "JOHN"
 ]

# Ejemplo de set comprehension con condición:
{name.lower().strip() for name in usernames}

# Operaciones con conjuntos

#UNION
pet_animals = {"dog", "cat", "hamster", "parrot"}
farm_animals = {"cow", "chicken", "goat", "dog", "cat"}

pet_animals | farm_animals
pet_animals.union(farm_animals)

farm_animals | pet_animals
pet_animals | farm_animals
farm_animals.union(pet_animals)


pet_animals | ["cow", "chicken", "goat", "dog", "cat"]

pet_animals.union(["cow", "chicken", "goat", "dog", "cat"])


a = {1, 2, 3, 4}
b = {2, 3, 4, 5}
c = {3, 4, 5, 6}
d = {4, 5, 6, 7}

a.union(b, c, d)

a | b | c | d


#INTERSECTION
john_friends = {"Linda", "Mathew", "Carlos", "Laura"}
jane_friends = {"Alice", "Bob", "Laura", "Mathew"}

john_friends & jane_friends


john_friends.intersection(jane_friends)

a = {1, 2, 3, 4}
b = {2, 3, 4, 5}
c = {3, 4, 5, 6}
d = {4, 5, 6, 7}

a & b & c & d


a.intersection(b, c, d)


x = {1, 2, 3, 4}
y = {5, 6, 7, 8}

x & y

#DIFERENCIA

registered_users = {"Alice", "Bob", "Charlie", "Diana", "Linda"}
checked_in_users = {"Alice", "Charlie", "Linda"}

registered_users - checked_in_users

checked_in_users - registered_users


a = {1, 2, 3, 30, 300}
b = {10, 20, 30, 40}
c = {100, 200, 300, 400}
d = {3, 4, 5}

a - b - c - d


a.difference(b, c)

#Diferencia simetrica
morning_attendees = {"Alice", "Charlie", "Linda", "John", "Jane"}
afternoon_attendees = {"Charlie", "Linda", "Bob", "Jane"}

morning_attendees ^ afternoon_attendees
afternoon_attendees ^ morning_attendees

morning_attendees.symmetric_difference(afternoon_attendees)


a = {1, 2, 3, 4, 5}
b = {10, 2, 3, 4, 50}
c = {1, 50, 100}

a ^ b ^ c

a.symmetric_difference(b, c) # ?
a.symmetric_difference(b).symmetric_difference(c)

# Operaciones aumentadas

# UNION
checked_in_attendees = set(["david"])
id(checked_in_attendees)

checked_in_attendees |= {"Alice", "Charlie"}
checked_in_attendees
id(checked_in_attendees)

checked_in_attendees.update({"Linda", "Bob"})
checked_in_attendees
id(checked_in_attendees)

# INTERSECCION
accepted_emails = {"Bob", "Diana", "Charlie"}

target_customers = {"Alice", "Bob", "Charlie", "Diana", "Jane"}
target_customers &= accepted_emails
target_customers


# DIFERENCIA
todo_list = {
    "Implement user login",
    "Fix bug #123",
    "Improve performance",
    "Write unit tests"
}

completed_tasks = {
    "Fix bug #123",
    "Improve performance"
}

todo_list.difference_update(completed_tasks)
todo_list

# Simetrica
morning_attendees = {"Alice", "Charlie", "Linda", "John", "Jane"}
afternoon_attendees = {"Charlie", "Linda", "Bob", "Jane"}

whole_day_attendees = set()
whole_day_attendees ^= morning_attendees
whole_day_attendees
whole_day_attendees.symmetric_difference_update(afternoon_attendees)
whole_day_attendees

# metodos comunes

estudiantes = {"Alexander", "Giovanny", "Jorge"}

estudiantes.add("Niccol")
estudiantes

estudiantes.remove("Jorge")
estudiantes.add("Jorge")
estudiantes.discard("Niccol")

estudiantes.remove("David")
estudiantes.discard("David")

estudiantes.pop()

estudiantes.clear()

estudiantes_2 = estudiantes.copy()
id(estudiantes)
id(estudiantes_2)
estudiantes_2
estudiantes_2.add("David")

for estudiante in estudiantes_2:
    print(f"El estudiante: {estudiante}")


# Continuación para tutoria

# COMPARACIÓN DE CONJUNTOS
#subsets

required_ingredients = {"cheese", "eggs", "milk"}
available_ingredients = {"cheese", "eggs", "milk", "sugar", "salt"}
required_ingredients <= available_ingredients
required_ingredients.issubset(available_ingredients)


a = {1, 2, 3, 4, 5}
a <= a
a.issubset(a)

#Proper subsets
regular_plan = {"Tutorials", "Quizzes"}
premium_plan = {"Tutorials", "Video Courses", "Quizzes", "Books"}

regular_plan < premium_plan

a = {1, 2, 3, 4, 5}

a < a

#Superset
required_ingredients = {"cheese", "eggs", "milk"}
available_ingredients = {"cheese", "eggs", "milk", "sugar", "salt"}

available_ingredients >= required_ingredients

available_ingredients.issuperset(required_ingredients)

a = {1, 2, 3, 4, 5}
a.issuperset(a)

a >= a

#Proper supersets
regular_plan = {"Tutorials", "Quizzes"}
premium_plan = {"Tutorials", "Video Courses", "Quizzes", "Books"}

premium_plan > regular_plan


a = {1, 2, 3, 4, 5}

a > a

#Disjoint sets


def verify_purchase(age, selection, restricted_products):
    if age < 18 and not selection.isdisjoint(restricted_products):
        print("Compra declinada: la selección contiene productos restringidos.")
    else:
        print("Compra aprobada!")

verify_purchase(
    age=15,
    selection={"leche", "pan", "cerveza"},
    restricted_products={"alcohol", "cerveza", "cigarrillos"}
)


verify_purchase(
    age=15,
    selection={"leche", "pan"},
    restricted_products={"alcohol", "cerveza", "cigarrillos"}
)


verify_purchase(
    age=25,
    selection={"leche", "pan", "cerveza"},
    restricted_products={"alcohol", "cerveza", "cigarrillos"}
)
