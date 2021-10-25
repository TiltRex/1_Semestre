a=int(input("Ingrese el primer numero: "))
b=int(input("Ingrese el segundo numero: "))
c=int(input("Ingrese el tercer numero: "))
d=int(input("Ingrese el cuarto numero: "))
e=int(input("Ingrese el quinto numero: "))

orden = [a, b, c, d, e]
orden.sort(reverse=True)

if a>b and a>c and a>d and a>e:
    print(a,"es el mayor")
elif b>c and b>d and b>e:
    print(b,"es el mayor")
elif c>d and c>e:
    print(c,"es el mayor")
elif d>e:
    print(d,"es el mayor")
else:
    print(e,"es el mayor")

print(orden)
