print("Identificador de numeros pares e impares")
print("-----------------------------------------")

num=float(input("Ingrese un numero: "))

if num==0:
    print(f"El numero ingresado es {int(num)}, por lo tanto no es par ni impar")
elif num%2==0:
    print(f"El numero ingresado es {num}, por lo tanto es par")
else:
    print(f"El numero ingresado es {num}, por lo tanto es impar")