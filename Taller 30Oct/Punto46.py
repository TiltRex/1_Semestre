print("Secuencia ascendente entre 2 numeros")
print("-------------------------------------------")

n=int(input("Ingrese desde que numero desea realizar la secuencia: "))
m=int(input("Ingrese hasta que numero desea realizar la secuencia: "))

if n<m:
    for x in range(n,m-1):
        n+=1
        print(n)
else:
    print("-------------------------------------------\nEsta solo es una secuencia ascendente,\nverifique que el segundo dato introducido sea mayor al primero")
