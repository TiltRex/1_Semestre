print("El mayor de 2 numeros")
print("----------------------")

list=[]
a=1

for x in range(2):
    num=float(input(f"Ingrese el {a}° numero: "))
    a+=1
    list.append(num)

mayor=list[0]
for x in range(2):
    if list[x]>mayor:
        mayor=list[x]

print(f"El numero mayor entre {list[0]} y {list[1]}, es: {mayor}")