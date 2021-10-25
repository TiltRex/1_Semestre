num1 = float(input("Introduzca el primer numero: "))
num2 = float(input("Introduzca el segundo numero: "))
num3 = float(input("Introduzca el tercer numero: "))

if num1 > num2 and num1 > num3:
    print("el numero mayor es el primero", num1)

elif num2>num3:
    print("el numero mayor es el segundo", num2)

else:
    print("el numero mayor es el tercer", num3)