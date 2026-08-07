print("---Calculadora---")

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "ERROR: No se puede dividir por 0"
    return a / b

opcion = input("Ingrese los numeros que desea operar \n 1-Sumar\n 2-Restar\n 3-Multiplicar\n 4-Dividir: ")

num1 = float(input("Ingrese el primer numero: "))
num2 = float(input("Ingrese el segundo numero: "))

if opcion == "1":
    print(sumar(num1, num2))
elif opcion == "2":
    print(restar(num1, num2))
elif opcion == "3":
    print(multiplicar(num1, num2))
elif opcion == "4":
    print(division(num1,num2))
else:
    print("Numero no valido")

