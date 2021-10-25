print("Calculadora de funciones de la forma ax^2+bx+c")
print("-------------------------------")

abc=["a","b","c"]
list=[]
a=0

for x in range(3):
    num=float(input(f"Ingrese el valor de {abc[a]}: "))
    list.append(num)
    a+=1

r1=(-list[1]+((list[1]**2)-4*list[0]*list[2])**0.5)
r1/=(2*list[0])
r2=(-list[1]-((list[1]**2)-4*list[0]*list[2])**0.5)
r2/=(2*list[0])

print(f"-------------------------------\nLa primera raiz es: {r1}")
print(f"La segunda raiz es: {r2}\n-------------------------------")