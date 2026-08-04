try:
    cuenta = float(input("Ingrese el total de la cuenta a pagar($): "))

    if cuenta > 0:
        propina = float(input("ingrese la cantidad de propina que desea abonar, ej 10, 20, 30: "))
        monto_propina = cuenta * (propina / 100)
        total = cuenta + monto_propina

        print(f"Monto de la Propina ${monto_propina:.2f}")
        print(f"Monto final a pagar ${total:.2f}")
    elif cuenta == 0:
        print("El monto debe ser mayor a 0")
    else:
        print("El monto no puede ser negativo")

except ValueError:
    print("Ingrese un numero valido")
    
    