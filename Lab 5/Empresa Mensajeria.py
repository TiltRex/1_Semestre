kg=int(input("Ingrese el peso en kilogramos: "))
km=int(input("Ingrese la distancia en kilometros: "))

p_kg=kg*int(1500)
p_km=km*int(4000)
pf= p_kg+p_km
pf15 = pf - pf * float(0.15)


if kg<int(10):
    print("El peso no es aceptable")

elif kg>int(100) and int(100)<km<int(2000):
    print("El precio a pagar es:",int(pf15))

elif kg>int(100) and km>=int(2000):
    pf15 = pf15 - pf15 * float(0.10)
    print("El precio a pagar es:",int(pf15))

elif kg>=int(10) and km>=int(2000):
    pf = pf - pf * float(0.10)
    print("El precio a pagar es:",int(pf))

else:
    print("El precio a pagar es:",pf)

