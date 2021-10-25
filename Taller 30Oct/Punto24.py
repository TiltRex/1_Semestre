print("Calculadora del IVA y descuento por compras superiores a 150.000")
print("--------------------")

ogv=int(input("Ingresa el valor de la compra: "))


if ogv<=0:
    print("Error\nIntente de nuevo")
elif ogv<150000:
    IVA=ogv*0.19
    tv=ogv*1.19
    print("El valor del IVA es:",IVA)
    print("El valor de la compra con IVA incluido es:",tv)
else:
    ogvD=ogv-ogv*0.05
    IVA=ogvD*0.19
    tv=ogvD*1.19
    print("El valor de la compra con descuento es:",ogvD)
    print("El valor del IVA es:",IVA)
    print("El valor de la compra con IVA incluido es:",tv)