print("Calculadora de suma y promedio de n numeros ingresados")
print("--------------------------------------------------------")

n=int(input("Cuantos numero desea introducir?: "))

a=1
b=0

for x in range(n):
    num=float(input(f"Ingrese el {a}° numero: "))
    a+=1
    b+=num

print("\nLa suma de los numeros ingresados es:",b)
print("El promedio de los numeros ingresados es:",b/n)