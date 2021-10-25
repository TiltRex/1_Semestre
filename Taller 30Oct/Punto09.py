print("Calculadora del promedio de 3 numeros")
print("--------------------------------------")

a=1
b=0

for x in range(3):
    num=float(input(f"Ingrese el {a}° numero: "))
    a+=1
    b+=num

print("El promedio de los numeros ingresados es:",b/3)