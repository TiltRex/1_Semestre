num=int(input("Dame un numero entero: "))
num2=int(input(f"Dame un numero entero mayor que, {num}: "))

if num2<num:
    print("¿Ya te cansaste? adios")
    exit()

while num2>num:
    num2=int(input(f"Dame un numero entero mayor que, {num2}: "))

##Falta Terminarlo
    