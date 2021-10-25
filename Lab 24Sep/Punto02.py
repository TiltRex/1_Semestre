print("Calculadora de suma de digitos")
print("Ingrese el 0 para acabar el programa\n")

def sumaDigitos(numero):
	suma=0
	while numero!=0:
	    digito=numero%10
	    suma=suma+digito
	    numero=numero//10
	return suma

num=int(input("Ingrese un numero: "))
while num!=0:
	print("Suma:",sumaDigitos(num))
	num=int(input("Ingrese un numero: "))
