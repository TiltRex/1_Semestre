print("Calculadora de Factorial de un numero")
print("Para interrumpir el programa ingrese -1" )
print("----------------------------------------\n")

def factorial(numero):
   f=1
   if numero!=0:
       for i in range(1,numero+1):
           f=f*i
   return f
cantidad=0
num=int(input("Ingrese un Número: "))
while num!=-1:
    print("Factorial:", factorial(num))
    cantidad+=1
    num=int(input("Ingrese un Número: "))
print("Se leyeron",cantidad,"números ingresados")
