print("Ingrese numeros hasta que se cumpla alguna de las siguientes condiciones:\n-Halla ingresado 10 numeros pares\n-Halla ingresado 20 numeros '5'")
print("-------------------------------------------------------------------------")

a=0
b=0
c=0

while a!=10:
    num=int(input("Ingrese un numero: "))
    if num<0:
        print("-------------------------")
        print("Solo se pueden ingresar numeros positivos\nPor favor vuelva a intentarlo")
        exit()
    elif num%2==0 and num>0:
        a+=1
    elif num==5:
        b+=1
        c+=1
        if b==20:
            break
    else:
        c+=1

print("-------------------------")
print("la cantidad de numeros introducidos fue:",a+b+c,"\n Donde:\n",a,"fueron numeros pares\n",b,"fueron numeros '5'\n",c,"fueron numeros impares")