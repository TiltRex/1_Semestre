print("Verificador de mayor y menor de numeros")
print("-------------------------------")

list=[]
a=1

for x in range(3):
    num=int(input(f"Ingrese el {a}° numero: "))
    list.append(num)
    a+=1

sum=list[0]+list[1]

if sum>list[2]:
    print(f"-------------------------------\nLa suma entre {list[0]} y {list[1]} es mayor a {list[2]}")
else:
    print(f"-------------------------------\nLa suma entre {list[0]} y {list[1]} es menor a {list[2]}")
