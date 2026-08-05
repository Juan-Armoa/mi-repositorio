print("-----Notas-----")

notas = []

for i in range(3):
    try:
        nota = float(input(f"Ingresa la nota {i + 1} (0-10): "))
        if 0 <= nota <= 10:
            notas.append(nota)
        else:
            print("Error: Ingrese un numero entre el 0 y 10")
    except ValueError:
        print("Error: Ingrese un numero valido")

if len(notas) > 0:
    nota_max = max(notas)
    nota_min = min(notas)
    promedio = sum(notas) / len(notas)

    print(f"Nota mas alta {nota_max:.2f}")
    print(f"Nota Minima {nota_min:.2f}")
    print(f"Nota Promedia {promedio:.2f}")

    if promedio >= 7:
        print("Estado: Aprobado")
    elif promedio >= 4:
        print("Estado: Regular")
    else:
        print("Estado: Desaprobado")
else:
    print("Error: No se ingresaron numeros validos")