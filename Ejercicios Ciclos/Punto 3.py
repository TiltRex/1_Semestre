list=[]
product = 1 
n=int(input("Ingrese un numero: "))


for x in range(n):
    list.append(n)
    n=n-1

for x in list:
    product = product*x

print("El factorial del numero ingresado es: ",product)