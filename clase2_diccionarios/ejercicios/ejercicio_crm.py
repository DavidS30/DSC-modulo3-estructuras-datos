clientes = {}
OPCION_ACTUALIZACION = {
    1: "Nombre",
    2: "Cedula",
    3: "Edad",
    4: "Email",
    5: "Telefono"
}
# Registro
while True:
    print("====* CRM de Clientes *=====")
    id_cliente = input("Digite un indentificador de cliente (o escriba 'salir' para terminar): ")
    if id_cliente.lower() == "salir":
        break
    if id_cliente in clientes:
        print("El cliente ya se encuentre registrado, digite otro ID")
        continue

    nombre = input("Digite el nombre del cliente: ")
    cedula = input("Digite la cedula del cliente:")
    edad = input("Digite la edad del cliente: ")
    email = input("Digite el email del cliente: ")
    telefono = input("Digite el telefono del cliente: ")

    clientes[id_cliente] = {
        "nombre": nombre,
        "cedula": cedula,
        "edad": edad,
        "email": email,
        "telefono": telefono
    }
    print(f"Su cliente con identificador: {id_cliente} ha sido registrado.")

# Menu
while True:
    print("===* Menu CRM Clientes *===")
    print("1. Ver los clientes registrados")
    print("2. Buscar cliente")
    print("3. Actualizar cliente")
    print("4. Salir")
    opcion = int(input("Elija una opción para el CRM:"))
    if opcion in [1,2,3,4]:
        if opcion == 1:
            print("\n Listado de clientes:")
            for id_cliente, data in clientes.items():
                print(f"- Cliente {id_cliente}: {data}")
        if opcion == 2:
            busqueda = input("Ingrese el id del cliente que quiere buscar: ")
            if busqueda in clientes:
                print(f" Datos del cliente {busqueda}: {clientes[busqueda]}")
            else:
                print("No existe este cliente.")
        if opcion == 3:
            busqueda = input("Ingrese el id del cliente que quiere buscar: ")
            if busqueda in clientes:
                print("=== Opciones disponibles ===")
                for op, nombre in OPCION_ACTUALIZACION.items():
                    print(f"{op}. {nombre}")
                opcion = input("Digite la opción que quiere modificar: ")
                match opcion:
                    case "1":
                        nuevo_nombre = input("Digite el nuevo nombre:")
                        clientes[busqueda]["nombre"] = nuevo_nombre
                    case "2":
                        nueva_cedula = input("Digite la nueva cedula:")
                        clientes[busqueda]["cedula"] = nueva_cedula
                    case "3":
                        nueva_edad = input("Digite la nueva edad:")
                        clientes[busqueda]["edad"] = nueva_edad
                    case "4":
                        nuevo_email = input("Digite el nuevo email")
                        clientes[busqueda]["email"] = nuevo_email
                    case "5":
                        nuevo_telefono = input("Digite el nuevo telefono:")
                        clientes[busqueda]["telefono"] = nuevo_telefono
                print(f"Usuario con id {busqueda} ha sido actualizado.")
        if opcion == 4:
            print("Saliendo del programa...")
            break
        else:
            print("La opción digitada no es valida.")
                
