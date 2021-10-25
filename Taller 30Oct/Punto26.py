print("Calculadora de notas")
print("-------------------------------")

list_nt=[]
list_p=[0.15,0.2,0.15,0.3,0.2]
a=1
n=0
t=0

while n!=5:
    n+=1
    nt=float(input(f"Ingrese la {a}° nota: "))
    list_nt.append(nt)
    a+=1
    if nt<0 or nt>5:
        n-=1
        list_nt.remove(nt)
        print("-------------------------------\nLa nota esta fuera del rango\nPor favor vuelve a introducirla\n-------------------------------")
        a-=1
        continue

for x in range(0,5):
    prcj=list_nt[x]*list_p[x]
    t+=prcj


if t<2:
    print("No puede habilitar")
elif t>=2 and t<3:
    print("Reprobo")
elif t>=3 and t<4.5:
    print("Aprobo")
else:
    print("Felicitaciones")