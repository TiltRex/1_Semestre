año=int(input("Ingrese un año: "))

if año%int(4)==int(0) and año%int(100)!=0 or año%int(400)==0:
    print(año,"es bisiesto") 
else:
    print(año,"no es bisiesto") 