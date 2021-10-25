print("Conversor de numero a dia de la semana")
print("-------------------------------")

list=["null","Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo"]

n=int(input("Ingresa un numero: "))

if n<=0 or n>7:
    print("Numero fuera del rango")
else:
    print(f"el {n} equivale a {list[n]}")