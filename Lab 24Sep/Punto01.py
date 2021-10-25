def validar(email):
    b= a.count("@")
    if b == 1:
        return True
    return False

a=input("Introduce tu Email: ")
if validar(a):
    print("Dirección válida")
else:
    print("Dirección inválida")
    print("Por favor ingrese tu email con @")