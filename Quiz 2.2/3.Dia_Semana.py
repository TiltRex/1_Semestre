dia=int(input("Introduce un dia de la semana (entre 1 y 7): "))
DS=["Incorrecto","Lunes","Martes","Miercoles","Jueves","Viernes","Festivo","Festivo"]

if dia>=8 or dia==0:
    print("El dato introducido no es correcto\nRecuerde introducir un numero entre 1 y 7")
elif dia>0 or dia<=7:
    print("El dia es ... ",DS[dia])
    