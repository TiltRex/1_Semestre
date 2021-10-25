import time

print("Conversor de segundos a horas-minutos-segundos")
print("--------------------------------")

t=int(input("Ingrese el numero de segundos que quiere convertir: "))

print(time.strftime("%H:%M:%S", time.gmtime(t)))