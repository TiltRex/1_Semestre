print("Calculadora de suma de numeros y digitos")
print("Ingrese el 0 para acabar el programa y mostrar resultados\n")

def sumaDigitos(numero): 
    suma=0 
    while numero!=0:  
        digito=numero%10 
        suma=suma+digito 
        numero=numero//10 
    return suma 
sumatoria=0 
num=int(input("Ingrese un numero: ")) 
while num!=0: 
    print("Suma:",sumaDigitos(num)) 
    sumatoria=sumatoria+num 
    num=int(input("Ingrese un numero: ")) 
print("Sumatoria:", sumatoria) 
print("Dígitos:", sumaDigitos(sumatoria)) 
