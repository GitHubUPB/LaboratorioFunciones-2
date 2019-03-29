def a_power_b (a,b):
    prod=1
    for x in range (1,b+1):
        if x>=1000:
            raise StopIteration("No Se Pudo")
        
        prod=prod*a
    return prod

potencia=0
par=0
impar=0
error=0

while True:

    try:
        potencia=potencia+1
        bas=int(input("ingrese la base"))
        if bas ==0:
            print("numero es cero ####")
            break
        exp=int(input("ingrese el exponente"))
        result=a_power_b(base,exponente)
        print("el resultado de su potencia es: ",result)
        if result % 2 ==0:
            par=par+1
        else:
            impar=impar+1
    except ValueError:
        error=error+1
        print("ingreso una letra")
    except StopIteration:
        error=error+1
        print("sobrepaso el limite")


print("las potencias que intento calcular  son: ",potencia)
print("los resultados pares son: ",par)
print("los resultados impares son: ",impar)
print("la cantidad de errores son: ",error)
