print("Clasificacion de numeros")
print("--------------------------------------------------------")

n=int(input("Cuantos numero desea introducir?: "))

a=1

b=0
c=0
d=0
e=0
f=0

for x in range(n):
    num=int(input(f"Ingrese el {a}° numero: "))
    a+=1
    if num>=0:
        b+=1
        if num%2==0:
            d+=1
            if num%8==0:
                f+=1
        else:
            e+=1
    elif num<0:
        c+=1
        if num%2==0:
            d+=1
            if num%8==0:
                f+=1
        else:
            e+=1
    

print(f"-----------------------------------\nEl total de numeros positivos es: {b}")
print(f"El total de numeros negativos es: {c}")
print(f"El total de numeros pares es: {d}")
print(f"El total de numeros impares es: {e}")
print(f"El total de numeros que son multiplos de 8 es: {f}")