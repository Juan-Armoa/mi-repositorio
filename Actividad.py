print("Bienvenido a mi calculadora infinita")


numero = None
resultado = ""
while True:
    if not resultado:
        resultado = (input("Ingrese un número: "))
        if resultado.lower() == "salir":
            break   
        resultado = int(resultado)
    op = input("Ingrese su operación: ")
    if op.lower() == "salir":
        break
    n2 = input ("Ingrese su segundo número: ")
    if n2.lower() == "salir":
        break
    n2 = int(n2)
    
    if op.lower()== "suma":
        resultado += n2
    elif op.lower() == "resta":
        resultado -= n2
    elif op.lower() == "multi":
        resultado *= n2
    elif op.lower() == "div":
        resultado /= n2
    else:
        print("Operación no válida, ingrese una operación válida")
        continue
        
    print("El resultado es: ", resultado)
    