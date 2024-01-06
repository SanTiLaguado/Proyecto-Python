clientes = [
    {"id": 1, "nombre": "Juan", "apellido": "Gómez", "edad": 30},
    {"id": 2, "nombre": "María", "apellido": "López", "edad": 25},
    # Añade más clientes si es necesario
]

def eliminar_cliente():
    id_eliminar = int(input("Ingrese el número de identificación del cliente que desea eliminar: "))
    for cliente in clientes:
        if cliente['id'] == id_eliminar:
            print(f"Cliente encontrado - ID: {cliente['id']}, Nombre: {cliente['nombre']} {cliente['apellido']}, Edad: {cliente['edad']}")
            confirmacion = input("¿Está seguro de que desea eliminar este cliente? (S/N): ")
            if confirmacion.upper() == 'S':
                clientes.remove(cliente)
                print("Cliente eliminado exitosamente.")
            else:
                print("Operación cancelada.")
            return
    print("No se encontró ningún cliente con ese número de identificación.")

def menu():
    while True:
        print("\n--- Menú ---")
        print("1. Mostrar clientes")
        print("2. Modificar cliente")
        print("3. Eliminar cliente")
        print("4. Salir")
        opcion = int(input("Ingrese el número de opción: "))

        if opcion == 1:
            mostrar_clientes()
        elif opcion == 2:
            modificar_cliente()
        elif opcion == 3:
            eliminar_cliente()
        elif opcion == 4:
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

menu()
