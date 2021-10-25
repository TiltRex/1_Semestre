##punto 1
horasT = float(input("Ingrese el numero de horas trabajadas: "))
horasT_ex = float(horasT-40)

pago = int((horasT * 20000))
pago_ex = int(horasT_ex * 30000)


if horasT <= int(40):
    print("Se le pagara:",pago,"$")
else:
    print("Se le pagara:",pago_ex + 800000,"$")

print("------------------------------------------------")

##punto 2
compra = int(input("Ingrese el valor de la compra: "))
compra_20 = float(compra*20 / 100)
descuento = float(compra - compra_20)

if compra > int(1000):
    print("El valor a pagar es:",descuento,"$")
else:
    print("El valor a pagar es:",compra,"$")

print("------------------------------------------------")

##punto 3
num1 = float(input("Introduzca el primer numero: "))
num2 = float(input("Introduzca el segundo numero: "))
num3 = float(input("Introduzca el tercer numero: "))

if num1 > num2 and num1 > num3:
    print("el numero mayor es el primero", num1)

elif num2>num3:
    print("el numero mayor es el segundo", num2)

else:
    print("el numero mayor es el tercer", num3)

print("------------------------------------------------")

##punto 4
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

print("------------------------------------------------")

##punto 5.1
edad = int(input("Introduzca su edad en años: "))

while edad < int(0):
    print("Introduzca un valor correcto")
    edad = int(input("Introduzca su edad en años: "))
    print("")

if edad >= int(18):
    print("Eres mayor de edad")
else:
    print("Fin del algoritmo")

print("------------------------------------------------")

##punto 5.2
n1=float(input("Introduzca el primer numero: "))
n2=float(input("Introduzca el segundo numero: "))

if n1 == n2:
    print('Los numeros son iguales')
else:
    print('Los numeros son diferentes')

print("------------------------------------------------")

##punto 5.3
nota1= float(input("Ingrese la primera nota: "))
nota2= float(input("Ingrese la segunda nota: "))
nota3= float(input("Ingrese la tercera nota: "))
nota4= float(input("Ingrese la cuarta nota: "))

promedio = float((nota1+nota2+nota3+nota4)/4)

if promedio >= float(11.5):
    print("Aprobado")
else:
    print("Reprobado")