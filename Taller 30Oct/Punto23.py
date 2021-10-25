print("Identificador de numeros pares e impares positivos y negativos")
print("---------------------------------------------------------------")

num=int(input("Ingrese un numero: "))

if num>0 and num%2==0:
    print(num,"Es par positivo")
elif num>0 and num%2!=0:
    print(num,"Es impar positivo")
elif num<0 and num%2==0:
    print(num,"Es par negativo")
elif num<0 and num%2!=0:
    print(num,"Es impar negativo")
else:
    print("El 0 no es positivo ni negativo")