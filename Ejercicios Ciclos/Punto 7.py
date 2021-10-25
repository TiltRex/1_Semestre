num=int(input("Ingrese un numero entero que sea par: "))

if num%2==0:
    print("Gracias")

while num%2!=0:
    num=int(input("Ese no es par, intentalo de nuevo: "))
    if num%2==0:
        print("Ahora si fue un numero par")
        print("Gracias")