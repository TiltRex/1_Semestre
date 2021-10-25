h=int(input("Ingrese el numero de horas: "))

if  h<=int(1):
    print("No tiene que pagar")

elif h>int(1) and h<=int(3):
    ph= h*2000
    ph2= h*2500
    print("El valor a pagar para automovil es",ph)
    print("El valor a pagar para camioneta es",ph2)
    print("Las motos no tienen que pagar")

else:
    h = h-3
    ph= h*1000 + 6000
    ph2= h*1250 + 7500
    print("El valor a pagar para automovil es",ph)
    print("El valor a pagar para camioneta es",ph2)
    print("Las motos no tienen que pagar")