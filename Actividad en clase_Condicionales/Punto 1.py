horasT = float(input("Ingrese el numero de horas trabajadas: "))
horasT_ex = float(horasT-40)

pago = int((horasT * 20000))
pago_ex = int(horasT_ex * 30000)


if horasT <= int(40):
    print("Se le pagara:",pago,"$")
else:
    print("Se le pagara:",pago_ex + 800000,"$")