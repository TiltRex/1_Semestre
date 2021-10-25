print("Identificador de secuencia")
print("-------------------------------")

list=[]
a=1

for x in range(3):
    num=int(input(f"Ingrese el {a}° numero: "))
    list.append(num)
    a+=1

if list[0]<list[1] and list[1]<list[2]:
    print("-------------------------------\nLos numeros estan incrementando")
elif list[2]<list[1] and list[1]<list[0]:
    print("-------------------------------\nLos numeros estan disminuyendo")
else:
    print("-------------------------------\nLos numeros no incrementan, ni disminuyen")