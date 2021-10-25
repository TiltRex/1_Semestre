cond="si"
def sumaDigitos(numero):
  suma=0
  while numero!=0:
      digito=numero%10
      suma=suma+digito
      numero=numero//10
  return suma
cantidad=0
mayor=-1
numero=int(input("Ingrese un Número positivo: "))
while cond.lower()=="si":
    if numero>=0:
        while numero>=0:
            suma=sumaDigitos(numero)
            if suma > mayor:
                mayor=suma
                n_mayorsuma=numero
            if suma < 10:
                cantidad+=1
            print("Sumatoria de dígitos de",n_mayorsuma,":",mayor)
            print("Cantidad con sumatoria menor a 10:",cantidad)
            cond=input("¿Quiere ingresar otro valor? = ¿si o no?: ")
            if cond.lower()=="no" or cond.lower()!="si":
                print("Hasta luego, vuelva pronto.")
                break
            numero=int(input("Número positivo: "))
    else:
        print("El numero ingresado no es positivo\nPara la proxima, asegurate de que sea positivo")
        break
