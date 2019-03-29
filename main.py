
def a_power_b (a,b):
    prod=1
    for x in range (1,b):
        prod=prod*b
    for x in range (1,b+1):
        if x>=1000:
            raise StopIteration("No Se Pudo")

        prod=prod*a
    return prod



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
    try:
        bas=int(input("ingresar la base"))
        if bas ==0:
            print("numero es cero")
            break
        exp=int(input("ingresar el exponente"))
    except ValueError:
        print("ingreso una letra")
    except StopIteration:
        print("paso el limite")
