print("Inversor de digitos de un numero")
print("---------------------------------")

def inv(n):
    num = 0
    while n != 0:
        num = 10*num+n % 10
        n //= 10
    return num


num=int(input("Ingrese un numero: "))
num_inv = inv(num)
print("Los digitos escritos de forma inversa de",num,"es:",num_inv)