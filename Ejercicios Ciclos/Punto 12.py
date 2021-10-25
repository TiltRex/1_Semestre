num=int(input("Ingrese un numero entero: "))
list=[]

while num!=1:
    list.append(num)
    if num%2==0:
        num=int(num/2)
    elif num%2!=0:
        num=int((num*3)+1)

list.append(1)
print(list)