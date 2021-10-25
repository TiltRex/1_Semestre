print("Identificador de numeros primos")

cond="si"
def primo(num):
   for i in range(2,num):
       if num%i==0:           
           return False
   return True
while cond.lower() == "si":
    numero=int(input("\nIngrese un Número: "))
    if primo(numero):
        print("El",numero,"es primo\n")
    else:
        print("El",numero,"no es primo\n")
    cond=input("¿Quieres ingresar otro Número? ")
    if cond.lower() == "no":
        print("Hasta luego, vuelva pronto.")
