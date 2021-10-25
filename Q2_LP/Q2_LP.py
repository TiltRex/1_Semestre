##1
print("1. Ingresar cuatro datos numéricos enteros e imprimirlos al revés.")
print("")

DNum1 = int(input("Num1: "))
DNum2 = int(input("Num2: "))
DNum3 = int(input("Num3: "))
DNum4 = int(input("Num4: "))

print ("---------------")
print ("", DNum4, DNum3, DNum2, DNum1)

##2 
print("")
print("2. Realizar la carga de dos números enteros por teclado e imprimir su suma y su producto.")
print("")

Num1 = int(input ("Num1: "))
Num2 = int(input ("Num2: "))

print ("---------------")
print ('Suma:', int(Num1) + int(Num2)) 
print ('Producto:', int(Num1) * int(Num2))

##3
print("")
print("3. Realizar la carga del precio de un producto y la cantidad a llevar. Mostrar cuanto se debe pagar (se ingresa un valor entero en el precio del producto).")
print("")

pan = int(200)

print("Precio del pan:",pan,"pesos")
print ("---------------")

NoPan = int(input("Cantidad a llevar: "))
print("Total a pagar:", pan * NoPan, "pesos")