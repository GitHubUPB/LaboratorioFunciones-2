def a_power_b (a,b):
    prod=1
    for x in range (0,b):
        prod=prod*a
        return prod



bas=int(input("ingrese El Valor Para La Base"))
exp=int(input("ingrese El Valor Para La Exponencia"))

result=a_power_b(bas,exp)

print("el resultado de su potencia es: ",result)
