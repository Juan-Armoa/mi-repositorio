logs_prueba = [
    "2026-08-05|INFO|Inicio del sistema",
    "2026-08-05|ERROR|No se pudo conectar a la base de datos",
    "2026-08-05|WARNING|Uso de memoria alto",
    "2026-08-05|ERROR|Archivo no encontrado",
    "linea_con_formato_invalido"
]

with open("errores.txt", "w") as archivo_errores:

    for linea in logs_prueba:
        partes = linea.split("|")
        print(partes)
        
        if len(partes) == 3 and partes[1] == "ERROR":
            archivo_errores.write(linea + "\n")
            print("Error guardado ->", partes[2])