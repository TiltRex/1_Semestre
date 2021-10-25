print("Conversor de numeros (digito) a letras (del 0 al 10)")
print("-----------------------------------------------------")

n=int(input("Ingrese un numero: "))

list=["cero","uno","dos","tres","cuatro","cinco","seis","siete","ocho","nueve","diez"]

if n>=0 and n<=10:
    print(list[n].capitalize())
else:
    print("Numero incorrecto")