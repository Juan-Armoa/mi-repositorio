print("Datos")

contactos = [
    {"nombre": "Jose", "numero": "112124321", "gmail": "juan91@gmail.com", "Pais": "Argentina"},
    {"nombre": "Camila", "numero": "192524321", "gmail": "Camila9291@gmail.com", "Pais": "Argentina"},
    {"nombre": "Jose", "numero": "112124321", "gmail": "juan91@gmail.com", "Pais": "Argentina"},
    {"nombre": "Camila", "numero": "192524321", "gmail": "Camila9291@gmail.com", "Pais": "Argentina"}
]

while True:
    opcion = input("Seleccione una de las opciones \n1. Agregar contactos \n2. Ver contactos \n3. Buscar contactos por nombre \n4. Salir: ").strip()

    if opcion == "1":
        nuevo_nombre = input("Nombre: ").strip()
        nuevo_numero = input("Numero: ").strip()
        nuevo_gmail = input("Gmail: ").strip()
        nueva_ubicacion = input("Ubicación: ").strip()

        if nuevo_nombre and nuevo_numero:
            nuevo_contacto = {
                "nombre": nuevo_nombre,
                "numero": nuevo_numero,
                "gmail": nuevo_gmail,
                "Pais": nueva_ubicacion
            }
            contactos.append(nuevo_contacto)
            print("Contacto agregado con exito!")
        else:
            print("ERROR: ingrese un contacto valido")

    elif opcion == "2":
        if not contactos:
            print("ERROR: no tienes contactos agregados")
        else:
            print("Tus contactos")
            for c in contactos:
                print(f"- {c['nombre']}: {c['numero']} ({c['gmail']})")

    elif opcion == "3":
        busqueda = input("Ingrese el contacto que desea buscar: ").strip()
        encontrado = False

        for c in contactos:
            if c["nombre"].lower() == busqueda.lower():
                print(f"Contacto encontrado: {c['nombre']} - {c['numero']} ({c['gmail']})")
                encontrado = True
                break

        if not encontrado:
            print("ERROR: Contacto no encontrado")

    elif opcion == "4":
        print("Chau")
        break

    else:
        print("Opción no válida")