print("Secuencia con patron")
print("-------------------------------------------")

n=int(input("Ingrese hasta que numero desea realizar la secuencia: "))

a=1
for x in range(n):
    if a%2==0:
        print(a*-1)
    else:
        print(a)
    a+=1