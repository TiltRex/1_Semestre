import numpy as np

zs=int(input("Ingrese el largo del vector de 0: "))
zv=np.zeros((zs))

print(f"Este es su vector --> {zv}")
print("-----------------------")

ch=input("Desea remplazar algun valor del vector?: ")

if ch.lower()=="no":
    exit()
elif ch.lower()=="si":
    rz=int(input("Ingrese la pocision del 0 que quiere reemplazar: "))
    num=float(input("Ingrese el numero por el cual va a reemplazar el 0: "))
    zv[rz-1]=num
    print(f"Este es su vector --> {zv}")
else:
    exit()