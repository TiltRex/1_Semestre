print("Sustituidor de variables")
print("-------------------------")


a=int(input("Ingrese el valor de la primera variable: "))
b=int(input("Ingrese el valor de la segunda variable: "))

print(f"-----------------------\nValor Inicial de las variables:\na:{a}\nb:{b}")

a+=b
b=a-b
a-=b

print(f"-----------------------\nValor despues del cambio de variables:\na:{a}\nb:{b}")
