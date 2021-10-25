import numpy as np

list=[]
n=int(input("Cuantos datos quiere ingresar?: "))

print("Ingrese datos para convertir de Fahrenheit a Celsius: ")
for x in range(n):
    fval=float(input("---> "))
    list.append(fval)

F = np.array(list)
print(f"Valores en grados Fahrenheit --> {F}")
print(f"Valores en grados Celsius --> {5*F/9 - 5*32/9}") 
