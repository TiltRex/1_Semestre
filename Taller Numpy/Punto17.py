import numpy as np

list1=[]
list2=[]

for x in range(4):
    num=float(input("Ingrese numeros para la primera lista: "))
    list1.append(num)

a1 = np.array([list1])
print(f"Primeta lista ---> {a1} ")

for x in range(4):
    num=float(input("Ingrese numeros para la segunda lista: "))
    list2.append(num)

a2 = np.array([list2])
print(f"Segunda lista ---> {a2} ")

print("Comparacion de cada elemento entre las dos listas")
print(np.in1d(a1, a2))