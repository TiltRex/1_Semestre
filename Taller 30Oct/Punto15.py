print("Calculadora de distancia entre 2 puntos en un plano cartesiano")
print("----------------------------------------------")

x1x2=[]
y1y2=[]
a=1

for x in range(2):
    x12=int(input(f"Ingrese el valor de X{a}: "))
    x1x2.append(x12)
    y12=int(input(f"Ingrese el valor de Y{a}: "))
    a+=1 
    y1y2.append(y12)
d=(((x1x2[1]-x1x2[0])**2)+((y1y2[1]-y1y2[0])**2))**0.5 

print(f"La distancia entre los dos puntos es aproximadamente:","{0:.4f}".format(d))