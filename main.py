    prod=prod*a
        return prod



bas=int(input("ingresar la base"))
exp=int(input("ingresar el exponente"))


result=a_power_b(bas,exp)
while True:

    bas=int(input("ingresar la base"))
    if bas ==0:
        print("numero es cero")
        break
    exp=int(input("ingresar el exponente"))
    result=a_power_b(bas,exp)
    print("el resultado de su potencia es: ",result)
    if bas ==0:
        break

print("el resultado de su potencia es: ",result)
