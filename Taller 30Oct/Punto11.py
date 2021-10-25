print("Calculadora de tiempo de caida desde una altura h")
print("--------------------------------------------------")

h=int(input("Ingrese la altura en metros desde donde cae el objeto: "))

G=9.8
t=((2*h)/G)**0.5

print("El objeto tardara","{0:.3f}".format(t),"segundos en caer")