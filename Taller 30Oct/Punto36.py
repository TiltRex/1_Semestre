print("Calculadora de digitos de un numero")
print("-------------------------------")


num=int(input("Ingrese un numero positivo menor a 100.000: "))

if num>100000 or num<0:
    print("Numero fuera del rango")
else:
    a=len(str(num))
    print(f"{num} tiene {a} digitos")