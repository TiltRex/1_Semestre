import numpy as np
list=[]

n=int(input("Cuantos datos numericos quiere ingresar: "))

for x in range(n):
    num=float(input("Ingrese datos numericos: "))
    if int(num)-num==0:
        list.append(round(num))
    else:
        list.append(num)

print(f"Lista original --> {list}")
print(f"Lista numpy unidimensional --> {np.array(list)}")