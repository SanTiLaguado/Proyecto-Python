import json
import os


def load_campers_json():
    try:
      with open(os.path.join("data", "campers.json"), 'r') as archivo_json:        
        lista_campers = json.load(archivo_json)
        print("La lista de campers ha sido guardada")
        return lista_campers
    except Exception as e:
      print(f"Error al guardar el archivo: {e}")

lista_campers = load_campers_json()

def crear_camper():
    nombre = input("Ingrese el nombre del camper: ")
    apellido = input("Ingrese el apellido del camper: ")
    edad = int(input("Ingrese la edad del camper: "))
    identificacion = (input("Ingrese el numero de identificacion: "))
    email = input("Ingrese el correo electrónico del camper: ")
    telefono = input("Ingrese el número de teléfono del camper: ")
    direccion = input("Ingrese la dirección del camper: ")
    print("----------- Datos del Acudiente-----------")
    acudiente = input("Ingrese el nombre del acudiente o contacto de emergencia: ")
    numerocont = input("Ingrese el número de teléfono del contacto: ")
    notaprueba = 0
    rutas = 'inscrito'
    estado = 'inscrito'

    camper = {
        'nombre': nombre,
        'apellido': apellido,
        'identificacion': identificacion,
        'notaprueba': notaprueba,
        'rutas': rutas,
        'edad': edad,
        'email': email,
        'telefono': telefono,
        'direccion': direccion,
        'estado': estado,
        'acudiente': acudiente,
        'numerocont': numerocont
    }

    lista_campers.append(camper)
    print("Se creó el camper con éxito")
    guardar_json()




def guardar_json():
    try:
      with open(os.path.join("data", "campers.json"), 'w') as archivo_json:
        json.dump(lista_campers, archivo_json, indent=2)
        print("La lista de campers ha sido guardada")
    except FileNotFoundError:
        print("El archivo no existe. Puede que aún no haya campers guardados.")
    except json.JSONDecodeError:
        print("Error al decodificar el archivo JSON . El formato podría ser incorrecto.")
    except Exception as e:
        print("Error desconocido:")
      

      

def listar_campers():
    print("Listado de campers: ")
    for camper in lista_campers:
        print(camper)

def modificar_campers():
    id_buscar = input("Ingrese el número de identificación del camper: ")
    for camper in lista_campers:
        if camper['identificacion'] == id_buscar:
            print(f"ID: {camper['identificacion']}, Nombre: {camper['nombre']} {camper['apellido']}, Edad: {camper['edad']}")
            opcion = int(input("Seleccione qué campo desea modificar:\n1. ESTADO\n2. Nota prueba ing\n3. Nombre\n4. Apellido\n5. Edad\n6. Email\n7. Telefono\n8. Direccion\n9. SALIR\nIngrese el número de opción: "))
            if opcion == 1:
                camper['estado'] = input("Ingrese el nuevo ESTADO: ")
            elif opcion == 2:
                camper['notaprueba'] = input("Ingrese la nota (Prueba de ingreso): ")
            elif opcion == 3:
                camper['nombre'] = input("Ingrese el nuevo nombre: ")
            elif opcion == 4:
                camper['apellido'] = input("Ingrese el nuevo apellido: ")
            elif opcion == 5:
                camper['edad'] = int(input("Ingrese la nueva edad: "))
            elif opcion == 6:
                camper['email'] = input("Ingrese el nuevo email: ")
            elif opcion == 7:
                camper['telefono'] = int(input("Ingrese el nuevo telefono: "))
            elif opcion == 8:
                camper['direccion'] = input("Ingrese la nueva direccion: ")
            elif opcion == 9:
                print("Saliendo")
                break           
            else:
                print("Opción inválida.")
            return
        else:
            print("No se encontró ningún camper con ese número de identificación.")
            break
guardar_json()

def eliminar_campers():
    id_eliminar = input("Ingrese el número de identificación del camper que desea eliminar: ")
    for camper in lista_campers:
        if camper['identificacion'] == id_eliminar:
            print(f"Camper Encontrado - ID: {camper['identificacion']}, Nombre: {camper['nombre']}, Apellido: {camper['apellido']}, Edad: {camper['edad']}")
            confirmacion = input("¿Está seguro de que desea ELIMINAR ESTE CAMPER? (SI/NO): ")
            if confirmacion.upper() == 'SI':
                lista_campers.remove(camper)
                print("El camper se elimino exitosamente.")
            else:
                print("Operación cancelada.")
            return
    else:
        print("No se encontró ningún camper con ese número de identificación.")
guardar_json()