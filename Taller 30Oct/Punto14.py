print("Calculadora de energia con la formula: E=mc^2")
print("----------------------------------------------")

kg=float(input("Ingrese la masa en kg: "))
C=299792458 
e=kg*C**2 

print(f"La energia es aproximadamente:","{0:.6f}".format(e),"Joules")