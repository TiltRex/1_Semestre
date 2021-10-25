print("Validador de documentos de identidad\n------------------------------------")
cond="si"
def frecuencia(numero):
   cantidad=0
   while numero!=0:
       ultDigito=numero%10
       cantidad+=1
       numero=numero//10
   return cantidad
while cond.lower()=="si":
    hi=input("""Que desea ingresar:
    1.Cedula de ciudadania
    2.Tarjeta de identidad
      ---> """)
    num=int(input("Ingrese el numero de su documento: "))
    if frecuencia(num)<4 and frecuencia(num)<12:
        print("El numero del documento es invalido")
    else:
        print("El numero del documento es valido")
        cond="no"
    cond=input("¿Quieres volver a ingresar?= ¿si o no?: ")
    if cond.lower() =="no":
        print("Hasta luego, vuelva pronto.")
