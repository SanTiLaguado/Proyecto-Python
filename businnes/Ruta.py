import json
from businnes.Campers import lista_campers,load_campers_json

lista_campers = load_campers_json()

rutas = {'NodeJS':[],'Java':[],'NetCore':[]}

def rutacampers(campers):
    
        seleccion = int(input('Escoja una opción:\n 1. Crear ruta \n 2. Asignar ruta a camper \n'))
        if seleccion == 1:

            op1 = int(input("Seleccione la ruta que desea crear: \n1. Fundamentos de programación (Introducción a la algoritmia, PSeInt y Python) \n2. Programación Web (HTML, CSS y Bootstrap) \n3. Programación formal (Java, JavaScript, C#) \n4. Bases de datos (Mysql, MongoDb y Postgresql) \n5. Backend (NetCore, Spring Boot, NodeJS y Express)\n"))
            while True:
                if op1 == 1:
                    fundamentosProgramacion = int(input("Seleccione la ruta principal a la que desea añadir: \n 1. NodeJS \n 2. Java \n 3. NetCore\n"))
                    if  fundamentosProgramacion== 1:
                        rutas['NodeJS'].append('Fundamentos de programación')
                
                    elif fundamentosProgramacion == 2:
                        rutas['Java'].append('Fundamentos de programación')
                
                    elif fundamentosProgramacion == 3:
                        rutas['NetCore'].append('Fundamentos de programación')
                    break
                elif op1 == 2:
                    programacionWeb = int(input("Seleccione la ruta principal a la que desea añadir: \n 1. NodeJS \n 2. Java \n 3. NetCore"))
                    if programacionWeb == 1:
                        rutas['NodeJS'].append('Programación Web')
                    elif programacionWeb == 2:
                        rutas['Java'].append('Programación Web')
                    elif programacionWeb == 3:
                        rutas['NetCore'].append('Programación Web')
                    break
                elif op1 == 3:
                    programacionFormal = int(input("Seleccione la ruta principal a la que desea añadir: \n 1. NodeJS \n 2. Java \n 3. NetCore"))
                    if programacionFormal == 1:
                        rutas['NodeJS'].append('Programación formal')
                    elif programacionFormal == 2:
                        rutas['Java'].append('Programación formal')
                    elif programacionFormal == 3:
                        rutas['NetCore'].append('Programación formal')
                    break
                elif op1 == 4:
                    basesDatos = int(input("Seleccione la ruta principal a la que desea añadir: \n 1. NodeJS \n 2. Java \n 3. NetCore"))
                    if basesDatos == 1:
                        rutas['NodeJS'].append('Bases de datos')
                    elif basesDatos == 2:
                        rutas['Java'].append('Bases de datos')
                    elif basesDatos == 3:
                        rutas['NetCore'].append('Bases de datos')
                    break
                elif op1 == 5:
                    backend = int(input("Seleccione la ruta principal a la que desea añadir: \n 1. NodeJS \n 2. Java \n 3. NetCore"))
                    if backend == 1:
                        rutas['NodeJS'].append('Backend')
                    elif backend == 2:
                        rutas['Java'].append('Backend')
                    elif backend == 3:
                        rutas['NetCore'].append('Backend')
                    break

        if seleccion == 2:
            id_buscar = input("Ingrese el número de identificación del camper: ")
            for camper in lista_campers:
                if camper['identificacion'] == id_buscar:
                    op2 = int(input("Las rutas disponibles para el camper son las siguientes:\n 1. Ruta NodeJS \n 2. Ruta Java \n 3. Ruta NetCore\n"))
                while True:
                    if op2 == 1:
                        camper['rutas'] = 'NodeJS'
                        break
                    elif op2 == 2:
                        camper['rutas'] = 'Java'
                        break
                    elif op2 == 3:
                        camper['rutas'] = 'NetCore' 
                        break
                else:
                    print("El camper no se encuentra inscrito")
        





