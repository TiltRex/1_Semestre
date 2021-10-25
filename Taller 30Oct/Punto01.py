name=input("Ingresa tu Nombre: ")

ch=input("¿Quieres agregar un calificativo a tu nombre? ")

if ch.lower()=="no":
    print(f"---------------\nTu nombre ---> {name.capitalize()}\nVuelve pronto")
elif ch.lower()=="si":
    ch2=int(input("¿Como le gustaria el calificativo:?\n1.Predeterminado\n2.Personalizado\n--->"))
    if ch2==1:
        print(f"---------------\n{name.capitalize()} el/la mejor\nVuelve pronto")
    elif ch2==2:
        add=input("Ingresa el calificativo: ")
        print(f"---------------\n{name.capitalize()} {add}\nVuelve pronto")
    else:
        print("---------------\nOpcion no valida\nVuelve pronto")
else:
    print("---------------\nOpcion no valida\nVuelve pronto")

