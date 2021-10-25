print("Calculadora de n digitos en x numero\n")
cond="si"
def frecuencia(numero,digito):
   cantidad=0
   while numero!=0:
       ultDigito=numero%10
       if ultDigito==digito:
           cantidad+=1
       numero=numero//10
   return cantidad
while cond.lower()=="si":
    num=int(input("Ingrese un Número: "))
    un_digito=int(input("Ingrese un Dígito: "))
    print("Frecuencia del dígito en el número:",frecuencia(num,un_digito))
    cond=input("Quieres volver a ingresar un numero y un digito = ¿si o no?: ")
    if cond.lower() =="no":
        print("Hasta luego, vuelva pronto.")
