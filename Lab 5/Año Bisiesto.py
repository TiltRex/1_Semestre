año=2021

while año!=int(0):
    año=año-int(1)
    if año%int(4)==int(0) and año%int(100)!=0 or año%int(400)==0:
        print(año) 


