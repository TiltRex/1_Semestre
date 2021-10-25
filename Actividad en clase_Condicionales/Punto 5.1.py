edad = int(input("Introduzca su edad en años: "))

while edad < int(0):
    print("Introduzca un valor correcto")
    edad = int(input("Introduzca su edad en años: "))
    print("")

if edad >= int(18):
    print("Eres mayor de edad")
else:
    print("Fin del algoritmo")
