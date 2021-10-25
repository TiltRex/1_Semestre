print("Identificador de numeros positivos y negativos")
print("-----------------------------------------------")

num=float(input("Ingrese un numero: "))

if num==0:
    print(f"El numero ingresado es {int(num)}, por lo tanto no es positivo ni negativo")
elif num>0:
    print(f"El numero ingresado es {num}, por lo tanto es positivo")
else:
    print(f"El numero ingresado es {num}, por lo tanto es negativo")

