nota1= float(input("Ingrese la primera nota: "))
nota2= float(input("Ingrese la segunda nota: "))
nota3= float(input("Ingrese la tercera nota: "))
nota4= float(input("Ingrese la cuarta nota: "))

promedio = float((nota1+nota2+nota3+nota4)/4)

if promedio >= float(11.5):
    print("Aprobado")
else:
    print("Reprobado")