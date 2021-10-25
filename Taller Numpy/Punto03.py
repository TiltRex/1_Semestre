import numpy as np

list=[]
ch=int(input("Que desea realizar?\n1)Matriz por defecto\n2)Matriz personalizada\n--->"))

if ch<1 or ch>2:
    exit()
elif ch==1:
    mpd= np.arange(2, 11).reshape(3,3)
    print(mpd)
else:
    lm=int(input("Ingrese el largo de la matriz: "))
    am=int(input("Ingrese el alto de la matriz: "))
    for x in range(lm*am):
        num=float(input("Ingrese los numeros para la matriz: "))
        if int(num)-num==0:
            list.append(round(num))
        else:
            list.append(num)
    mp= np.array(list).reshape(am,lm)
    print(mp)