age=int(input("Introduzca la edad del piloto: "))

if age<int(18):
    print("El piloto es muy joven")
    exit()
elif age>=int(65):
    print("El piloto es muy viejo")
    exit()

ft=input("¿Realizo un vuelo nacional o intercional? ")
anf='a'
anf2='b'
inter=int(0)
nac=int(0)

if ft.lower()=='nacional':
    nac=1
    km=int(input("Ingrese la distancia del vuelo en kilometros: "))
    anf=input("¿Realizo algun otro vuelo nacional?: ")
    while anf.lower()=='si':
        nac=1+nac
        km=int(input("Ingrese la distancia del vuelo en kilometros: ")) + km
        anf=input("¿Realizo algun otro vuelo nacional?: ")
if anf.lower()=='no':
    anf=input("¿Realizo algun otro vuelo internacional?: ")
    if anf.lower()=='si':
        inter=1
        km=int(input("Ingrese la distancia del vuelo en kilometros: ")) + km
        while anf.lower()=='si':
            anf=input("¿Realizo algun otro vuelo internacional?: ")
            if anf.lower()=='si':
                inter=1+inter
                km=int(input("Ingrese la distancia del vuelo en kilometros: ")) + km


if ft.lower()=='internacional':
    inter=1
    km=int(input("Ingrese la distancia del vuelo en kilometros: "))
    anf2=input("¿Realizo algun otro vuelo internacional?: ")
    while anf2.lower()=='si':
        inter=1+inter
        km=int(input("Ingrese la distancia del vuelo en kilometros: ")) + km
        anf2=input("¿Realizo algun otro vuelo internacional?: ")
if anf2.lower()=='no':
    anf2=input("¿Realizo algun otro vuelo nacional?: ")
    if anf2.lower()=='si':
        nac=1
        km=int(input("Ingrese la distancia del vuelo en kilometros: ")) + km
        while anf2.lower()=='si':
            anf2=input("¿Realizo algun otro vuelo nacional?: ")
            if anf2.lower()=='si':
                nac=1+nac
                km=int(input("Ingrese la distancia del vuelo en kilometros: ")) + km

if int(18)<=age<=int(50):
    fh=float(km/int(893))
elif int(50)<age<int(65):
    fh=float(km/int(893)*(1.20))

tf=input("¿Realizo un vuelo el dia anterior?: ")
nf='c'

if tf.lower()=='si':
    nf=input("¿Su siguiente vuelo sera internacional?: ")
elif tf.lower()=='no':
    tfh=fh+nac+inter*2

if nf.lower()=='si':
    tfh=fh+nac+inter*2+1
elif nf.lower()=='no':
    tfh=fh+nac+inter*2

if tfh<=int(40):
    print("El piloto aun puede volar, le quedan aproximadamente,",round(int(40)-tfh),"horas de vuelo")
else:
    print("El piloto no puede volar, sobrepaso su limite de horas aproximadamente por,",round(tfh-int(40)),"horas de vuelo")