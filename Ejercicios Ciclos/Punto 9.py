print("1. Suma \n2. Resta \n3. Multiplicacion \n4. Division \n\n0. Terminar\n" )
op=int(input("¿Que operacion desea realizar?: "))

if op==0:
    print("Hasta pronto")

while op!=0:
    if op==1:
        num1=float(input("Ingrese el primer numero: "))
        num2=float(input("Ingrese el segundo numero: "))
        print("--------------------")
        print("El resultado es:",num1+num2)
    elif op==2:
        num1=float(input("Ingrese el primer numero: "))
        num2=float(input("Ingrese el segundo numero: "))
        print("--------------------")
        print("El resultado es:",num1-num2)
    elif op==3:
        num1=float(input("Ingrese el primer numero: "))
        num2=float(input("Ingrese el segundo numero: "))
        print("--------------------")
        print("El resultado es:",num1*num2)
    elif op==4:
        num1=float(input("Ingrese el primer numero: "))
        num2=float(input("Ingrese el segundo numero: "))
        print("--------------------")
        print("El resultado es:",num1/num2)
    else:
        print("Ingrese una opcion valida")
    print("--------------------")
    print("\n1. Suma \n2. Resta \n3. Multiplicacion \n4. Division \n\n0. Terminar\n" )
    op=int(input("¿Que operacion desea realizar?: "))
    if op==0:
        print("Hasta pronto")