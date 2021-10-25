num=int(input("Ingrese un numero: "))

if (num%int(2)==0 and num%int(7)!=0 and num%int(9)!=0) or (num>int(100) and num<int(5000) and num%int(2)!=2 and num%int(7)!=0 and num%int(5)==0):
    print(num,"Es un numero chevere")

else:
    print(num,"No es un numero chevere")
