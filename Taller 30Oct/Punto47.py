print("Suma de los numeros comprendidos entre 2 numeros")
print("-------------------------------------------")

n=int(input("Ingrese desde que numero desea realizar la secuencia: "))
m=int(input("Ingrese hasta que numero desea realizar la secuencia: "))
a=0
b=n

if n<m:
    for x in range(n,m-1):
        b+=1
        a+=b
    print(f"La suma de los numeros comprendidos entre {n} y {m} es: {a}")
else:
    print("-------------------------------------------\nError\nAsegurese que el segundo dato introducido sea mayor al primero")
