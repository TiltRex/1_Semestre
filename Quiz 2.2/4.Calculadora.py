#
#  
#
############################################-1-##################################################
def sumar(): #Definimos la función sumar
    x = a + b
    print (("El resultado es:"), (x))
def restar():#Definimos la función restar
    x = a - b
    print (("El resultado es:"), (x))
def multiplicar():#Definimos la función multiplicar
    x = a * b
    print (("El resultado es:"), (x))
def dividir():#Definimos la función dividir
    x = a / b
    print (("El resultado es:"), (x))
##########################################-2-###################################################
while True: #Se establece un bucle que siempre estara "activo" hasta que se obtangan los datos de entrada
    try: #Intentamos obtener los datos de entrada
        a = int(input("Ingresa el primer numero: \n")) #Se le pide al usuario ingresar el primer numero
        b = int(input("Ingresa el segundo numero: \n"))#Se le pide al usuario ingresar el segundo numero
        print (("Que cálculo quieres realizar entre los numeros:"), (a), ("y"), (b), ("?\n"))#Se le pide al usuario ingresar que calculo quiere realizar entre los 2 numeros ingresados
        op = str(input("1-Sumar\n2-Restar\n3-Multiplicar\n4-Dividir\n---> ")) #Ofrecemos las opciones de cálculo que van a llamar a las funciones
    except: #En caso de error:
        print ("Error")
        op = '?'
##########################################-3-##################################################
    if op == '1':#Si el usuario elige opción 1 llamamos a sumar
        sumar()
        break
    elif op == '2':#Si el usuario elige opción 2 llamamos a restar
        restar()
        break
    elif op == '3':#Si el usuario elige opción 3 llamamos a multiplicar
        multiplicar()
        break
    elif op == '4':#Si el usuario elige opción 4 llamamos a dividir
        dividir()
        break
    else:
        print ("""Has ingresado un numero de opcion erroneo""") #En caso que el número no se encuentre

