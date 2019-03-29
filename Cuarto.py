            print("numero es cero")
            break
        exp=int(input("ingrese el exponente"))
        result=a_power_b(bas,exp)
        print("el resultado de su potencia es: ",result)
    except ValueError:
        print("ingreso una letra")
    except StopIteration:    
