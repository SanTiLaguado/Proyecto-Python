clientes = [
    {"id": 1, "nombre": "Juan", "apellido": "Gómez", "edad": 30},
    {"id": 2, "nombre": "María", "apellido": "López", "edad": 25},
]

def mostrar_clientes():
    print("Lista de clientes:")
    for cliente in clientes:
        print(f"ID: {cliente['id']}, Nombre: {cliente['nombre']} {cliente['apellido']}, Edad: {cliente['edad']}")

def modificar_cliente():
    id_buscar = int(input("Ingrese el número de identificación del cliente que desea modificar: "))
    for cliente in clientes:
        if cliente['id'] == id_buscar:
            print(f"Cliente encontrado - ID: {cliente['id']}, Nombre: {cliente['nombre']} {cliente['apellido']}, Edad: {cliente['edad']}")
            opcion = int(input("Seleccione qué campo desea modificar:\n1. Nombre\n2. Apellido\n3. Edad\nIngrese el número de opción: "))
            if opcion == 1:
                cliente['nombre'] = input("Ingrese el nuevo nombre: ")
            elif opcion == 2:
                cliente['apellido'] = input("Ingrese el nuevo apellido: ")
            elif opcion == 3:
                cliente['edad'] = int(input("Ingrese la nueva edad: "))
            else:
                print("Opción inválida.")
            print("Cliente modificado exitosamente.")
            return
    print("No se encontró ningún cliente con ese número de identificación.")

mostrar_clientes()
modificar_cliente()
mostrar_clientes()
