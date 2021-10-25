print("Cantidad minima de billetes a entregar")
print("--------------------------------------------------------")

x=int(input("ingrese un valor: "))
bills=[100000, 50000, 20000, 10000, 5000, 2000, 1000]
totalbill={}

for i in bills:
    if x >= i :
        bill1 = x//i
        totalbill[f"billetes de {i}"] = bill1
        x=x-(i*bill1)

print(totalbill)