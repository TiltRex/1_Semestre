print("Calculadora de distancia")
print("-------------------------")

a=float(input("Ingrese el valor de la aceleracion en m/s^2: "))
v=float(input("Ingrese el valor de la velocidad en m/s: "))

t= v/a
d= (a*(t**2))/2 

print("La distancia recorrida es:",d,"m")