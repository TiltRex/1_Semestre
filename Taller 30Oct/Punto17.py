print("Conversor de segundos a minutos")
print("--------------------------------")

seg=int(input("Ingrese la cantidad de segundos que desea convertir: "))

while seg<=0 or seg<60:
    print("Por favor ingrese un numero mayor a 60")
    seg=int(input("Ingrese la cantidad de segundos que desea convertir: "))

if seg%60==0:
    print(seg,"segundos en minutos, es:",int(seg/60),"minutos")
elif seg%60!=0:
    print(seg,"segundos en minutos, es:",int(seg//60),"minutos y",int(seg-60*(seg//60)),"segundos")