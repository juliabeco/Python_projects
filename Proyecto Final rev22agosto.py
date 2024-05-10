# Proyecto Final - Alumna: Julia Becaria Coquet
# Julio 2023

# Programa para gestionar una agenda telefónica con los nombres y los teléfonos de los conocidos de una persona


dic_contacto = {}

# Función para mostrar el telefono de un contacto registrado en la agenda
def opcion1(dic_contacto):
    nombre = input("Introduce el nombre del contacto que deseas obtener su teléfono: ").strip()
    apellido = input("Introduce el apellido del contacto que deseas obtener su teléfono: ").strip()
    nombre_completo = (nombre + " " + apellido).lower()

    encontrado = False
    for contacto in dic_contacto.values():
        if contacto["nombre"] + " " + contacto["apellidos"] == nombre_completo:
            print(f"Teléfono: {contacto['telefono']}")
            encontrado = True
            break

    if not encontrado:
        print("No se encontró ningún contacto con ese nombre y apellido.")

    print("Volvemos al menú principal.\n")

# Función para añadir un contacto a la agenda
def opcion2(dic_contacto):
    nombre = input("Introduce el nombre del contacto: ").strip()
    while len(nombre) < 2:
        print("Nombre inválido (un sólo caracter)")
        nombre = input("Introduce el nombre del contacto: ")

    apellidos = input("Introduce los apellidos del contacto: ").strip()
    while len(apellidos) < 2:
        print("Apellido/s inválido/s (un sólo caracter)")
        apellidos = input("Introduce los apellidos del contacto: ")

    nombre = nombre.lower()  # Convertir a minúsculas
    apellidos = apellidos.lower()  # Convertir a minúsculas

    while True:
        telefono = input("Introduce el teléfono del cliente: ")
        while len(telefono) != 9 or not telefono.isdigit():
            print("Número de teléfono inválido")
            telefono = input("Introduce el teléfono del cliente: ")

        if telefono in dic_contacto:
            print("Ya existe un registro con este número de teléfono. Por favor, ingresa otro número.")
        else:
            # Creamos el diccionario con los datos del contacto
            nuevo_contacto = {
                "nombre": nombre,
                "apellidos": apellidos,
                "telefono": telefono,
            }

            # Añadimos el contacto al diccionario de contactos
            dic_contacto[telefono] = nuevo_contacto
            print("Contacto añadido correctamente\nVolvemos al menú principal.\n")
            break

# Función para eliminar un cliente
def opcion3(dic_contacto):
    nombre = input("Introduce el nombre del contacto que deseas eliminar: ").strip()
    apellido = input("Introduce el apellido del contacto que deseas eliminar: ").strip()

    nombre_completo = f"{nombre.lower()} {apellido.lower()}"
    if nombre_completo in [contacto["nombre"] + " " + contacto["apellidos"] for contacto in dic_contacto.values()]:
        for telefono, contacto in dic_contacto.items():
            if contacto["nombre"] + " " + contacto["apellidos"] == nombre_completo:
                del dic_contacto[telefono]
                print("Contacto eliminado correctamente.")
                break
    else:
        print("No se encontró ningún contacto con ese nombre y apellido.")

    print("Volvemos al menú principal.\n")



# Función para mostrar todos los contactos de la agenda
def opcion4(dic_contacto):
    if not dic_contacto:
        print("No hay contactos registrados en la agenda.")
    else:
        print("Lista de contactos:")
        for telefono, info_contacto in dic_contacto.items():
            print(f"Nombre: {info_contacto['nombre']}")
            print(f"Apellidos: {info_contacto['apellidos']}")
            print(f"Teléfono: {info_contacto['telefono']}")
            print()

    print("Volvemos al menú principal.\n")


# Función para salir del programa
def opcion5():

    print("\n"
          'Saliendo del menú.\n'
          "Gracias! =)\n"
          "Nos vemos en la próxima consulta.")
    input("Presiona Enter para salir...")
    return True

# Función para guardar los contactos en un archivo de texto separado por comas
def guardar_contactos(dic_contacto):
    with open("contactos.txt", "w") as file:
        for contacto in dic_contacto.values():
            linea = f"{contacto['nombre']},{contacto['apellidos']},{contacto['telefono']}\n"
            file.write(linea)

# Función para cargar los contactos desde el archivo de texto

def cargar_contactos():
    dic_contacto = {}
    try:
        with open("contactos.txt", "r") as file:
            for linea in file:
                nombre, apellidos, telefono = linea.strip().split(",")
                nuevo_contacto = {
                    "nombre": nombre,
                    "apellidos": apellidos,
                    "telefono": telefono,
                }
                dic_contacto[telefono] = nuevo_contacto
    except FileNotFoundError:
        pass
    return dic_contacto



# Función para mostrar Menú del programa

def menu():
    dic_contacto = cargar_contactos()

    salir = False
    while not salir:
        print('___________ MENU ___________')
        print('______ Bienvenida/a! =) ______')
        print('____ ¿Qué deseas hacer? ____')
        print()
        print("1. Opción 1 ---> Obtener un teléfono\n"
              "2. Opción 2 ---> Insertar un teléfono\n"
              "3. Opción 3 ---> Eliminar un teléfono\n"
              "4. Opción 4 ---> Listar todos los contactos\n"
              "5. Opción 5 ---> Salir \n     ")


        op = int(input('Seleccione una opción: '))

        if op == 1:
            opcion1(dic_contacto)
        elif op == 2:
            opcion2(dic_contacto)
        elif op == 3:
            opcion3(dic_contacto)
        elif op == 4:
            opcion4(dic_contacto)
        elif op == 5:
            salir = opcion5()

        else:
            print()
            print('Disculpe, esa opción no es posible.\n'
                  'Debe seleccionar una opción de 1 a 5.')

        # Al final del menú, guardar los contactos en el archivo de texto antes de salir
        guardar_contactos(dic_contacto)

print()

menu()