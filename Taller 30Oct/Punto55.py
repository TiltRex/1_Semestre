print("Factores de un numero ")
print("--------------------------------------------------------")

num=int(input("Ingrese un numero: "))

for x in range(1,num+1):
    if num%x==0:
        print(x)