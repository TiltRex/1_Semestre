print("Conversor de segundos a horas")
print("--------------------------------")

seg=int(input("Ingrese la cantidad de segundos que desea convertir: "))

while seg<=0 or seg<3600:
    print("Por favor ingrese un numero mayor a 3600")
    seg=int(input("Ingrese la cantidad de segundos que desea convertir: "))

if seg%3600==0:
    print(seg,"segundos en horas, es:",int((seg/3600)),"horas")
elif seg%60!=0:
    print(seg,"segundos en horas, es:",int(seg//3600),"horas,",int(seg-3600*(seg//3600))//60,"minutos y",int(seg-60*(seg//60)),"segundos")
