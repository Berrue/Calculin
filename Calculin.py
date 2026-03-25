def sumar(a,b):
    return a+b
def restar (a,b):
    return a-b
def dividir (a,b):
    return a/b
def multiplicar (a,b):
    return a*b
while True:
    print ("----- Bienvenido a Calculin -----")
    a = input("escribi el primer numero o 'salir' para cerrar el programa: ")
    if a.lower() == "salir":
        print ("Gracias por usar a Calculin")
        exit()
    try:
        a = float(a)
    except ValueError:
        print ("Ingresa un numero valido o escribi 'salir' para cerrar el programa")
        continue
    b = float(input("escribi el segundo numero: "))
    try:
        b = float(b)
    except ValueError:
        print ("ingresa un segundo numero valido")
        continue
    operador = input("escribi el operador: ")

    if operador == "+":
        print(sumar(a,b))
    elif operador == "-":
        print(restar(a,b))
    elif operador == "/":
        if b != 0:
            print (dividir(a,b))
        else:
            print("No se puede dividir por 0")
            continue
    elif operador == "*":
        print (multiplicar(a,b))
    else:
        print("ingresa un operador valido")
