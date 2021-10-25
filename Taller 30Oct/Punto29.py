print("Mayor y menor entre 3 numeros")
print("-----------------------------")

list=[]
a=1

for x in range(3):
    num=float(input(f"Ingrese el {a}° numero: "))
    a+=1
    list.append(num)

menor=list[0]
mayor=list[0]

for x in range(1,3):
    if list[x]<menor:
        menor=list[x]
    if list[x]>mayor:
        mayor=list[x]

print("El numero menor es:",menor)
print("El numero mayor es:",mayor)