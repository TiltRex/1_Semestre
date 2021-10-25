list=[]
x=1
cont=0

while x==1:
    age=int(input("Ingrese la edad: "))
    if age<0 or age>120:
        break
    list.append(age)
    cont=cont+1
    ana=input("Desea ingresar otra edad?: ")
    if ana.lower()=='si':
        continue
    elif ana.lower()=='no':
        break
    else:
        break

menor=list[0]
for x in range(1,cont):
    if list[x]<menor:
        menor=list[x]
print("La menor edad es:",menor)