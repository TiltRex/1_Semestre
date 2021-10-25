print("Calculadora de precios de tiquetes de avion")
print("-------------------------------")

km=int(input("Ingrese la distancia a recorrer en kilometros: "))
d=int(input("Ingrese los dias de estancia: "))

if km<=20:
    print("El total a pagar es: 100000$")
elif km>1000 and d>7:
    print(f"El total a pagar es: {(100000+(km-20)*5000)*0.75}$")
else:
    print(f"El total a pagar es: {(100000+(km-20)*5000)}$")