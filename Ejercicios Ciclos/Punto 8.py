num=int(input("Ingrese un numero entre 0 y 100, par, múltiplo de 3 y de 7: "))

if num>=0 and num<=100 and num%3==0 and num%7==0:
    print("Gracias")

while num<0 or num>100 or num%3!=0 or num%7!=0:
    num=int(input("Ese numero no cumple las condiciones, intentalo de nuevo: "))
    if num>=0 and num<=100 and num%3==0 and num%7==0:
        print("Ahora si cumple las condiciones")
        print("Gracias")