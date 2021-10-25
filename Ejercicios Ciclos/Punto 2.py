list=[]
n=int(input("Ingrese el numero de estudiantes: "))

for x in range(n):
    scr=float(input("Ingrese la nota: "))
    if scr<0 or scr>5.0:
        break
    list.append(scr)

menor=list[0]
mayor=list[0]

for x in range(1,n):
    if list[x]<menor:
        menor=list[x]
    if list[x]>mayor:
        mayor=list[x]

print("La menor nota es:",menor)
print("La mayor nota es:",mayor)