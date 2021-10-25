print("Calculadora de suma y promedio de 10 numeros ingresados")
print("--------------------------------------------------------")

a=1
b=0

for x in range(10):
    num=float(input(f"Ingrese el {a}° numero: "))
    a+=1
    b+=num

print("\nLa suma de los 10 numeros ingresados es:",b)
print("El promedio de los 10 numeros ingresados es:",b/10)