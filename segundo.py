def a_power_b (a,b):
    prod=1
    for x in range (0,b):
        prod=prod*a
    return prod


#codigo

while True:
    
    bas=int(input("ingrese la base"))
    if bas ==0:
        print("numero es cero ####")
        break
    exp=int(input("ingrese el exponente"))
    result=a_power_b(bas,exp)
    print("el resultado de su potencia es: ",result)
    if base ==0:
        break

