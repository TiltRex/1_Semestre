print("Calculadora de suma y promedio de n numeros pares e impares ingresados")
print("--------------------------------------------------------")

n=int(input("Cuantos numero desea introducir?: "))

a=1
b=0
c=0

cont1=0
cont2=0

for x in range(n):
    num=int(input(f"Ingrese el {a}° numero: "))
    a+=1
    if num%2==0:
        b+=num
        cont1+=1
    else:
        c+=num
        cont2+=1

print("\nEl promedio de los numeros pares ingresados es:",b/cont1)
print("El promedio de los numeros impares ingresados es:",c/cont2)