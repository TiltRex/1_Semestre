print("Validador de numero")
print("-------------------------------------------")

num=float(input("Ingrese un numero entero positivo: "))

if num>0 and num-int(num)==0:
    print(f"El numero {int(num)} es valido")

while num<0 or num-int(num)!=0:
    print(f"El numero {num} no es valido")
    num=float(input("Ingrese un numero entero positivo: "))
    if num>0 and num-int(num)==0:
        print(f"El numero {int(num)} es valido")