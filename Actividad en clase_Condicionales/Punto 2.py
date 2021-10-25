compra = int(input("Ingrese el valor de la compra: "))
compra_20 = float(compra*20 / 100)
descuento = float(compra - compra_20)

if compra > int(1000):
    print("El valor a pagar es:",descuento,"$")
else:
    print("El valor a pagar es:",compra,"$")