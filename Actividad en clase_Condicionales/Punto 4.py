num_dia = int(input("ingrese un numero del 1 al 7: "))

while num_dia > int(7) or num_dia < int(1):
    print("Introduzca un valor valido")
    num_dia = int(input("ingrese un numero del 1 al 7: "))
    print("")

if num_dia == int(1):
    print("La equivalencia del numero en dias de la semana es: Lunes")
elif num_dia == int(2):
    print("La equivalencia del numero en dias de la semana es: Martes")
elif num_dia == int(3):
    print("La equivalencia del numero en dias de la semana es: Miercoles")
elif num_dia == int(4):
    print("La equivalencia del numero en dias de la semana es: Jueves")
elif num_dia == int(5):
    print("La equivalencia del numero en dias de la semana es: Viernes")
elif num_dia == int(6):
    print("La equivalencia del numero en dias de la semana es: Sabado")
else:
    print("La equivalencia del numero en dias de la semana es: Domingo")