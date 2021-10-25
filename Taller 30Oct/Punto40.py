print("Igualdad entre numeros")
print("-------------------------------")

n1=float(input("Ingrese el 1° numero: "))
n2=float(input("Ingrese el 2° numero: "))
n3=float(input("Ingrese el 3° numero: "))

if n1==n2 and n1==n3:
    print("-------------------------------\nTodos los numeros son iguales")
elif n1==n2:
    print("-------------------------------\nel 1° y 2° numero son iguales")
elif n2==n3:
    print("-------------------------------\nel 2° y 3° numero son iguales")
elif n1==n3:
    print("-------------------------------\nel 1° y 3° numero son iguales")
else:
    print("-------------------------------\nNingun numero es igual a otro")