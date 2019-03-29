def a_power_b (a,b):
    prod=1
    for x in range (0,b):
        prod=prod*a
        return prod
    for x in range (1,b):
        prod=prod*b
    return prod
