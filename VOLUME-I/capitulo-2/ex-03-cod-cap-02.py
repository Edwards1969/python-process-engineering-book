"""
2.4.1 O laço for - pág 35
"""
massa = 2.0 # Kg

for v in range(0, 11, 2):   # velocidade de 0 a 100 m/s
    energia = 0.5 * massa * v**2
    print("v = ", v, "m/s -> Ec =", energia, "J" )