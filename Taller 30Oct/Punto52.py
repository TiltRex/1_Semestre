print("Numeros mayores y menores a 100")
print("--------------------------------------------------------")

n=int(input("Cuantos numero desea introducir?: "))

a=1

b=0
c=0
d=0

for x in range(n):
    num=int(input(f"Ingrese el {a}° numero: "))
    a+=1
    if num>100:
        b+=1
    elif num<100:
        c+=1
    else:
        d+=1

print(f"\nEl total de numeros mayores a 100 son: {b}")
print(f"El total de numeros menores a 100 son: {c}")
print(f"El total de numeros 100 introducidos es: {d}")