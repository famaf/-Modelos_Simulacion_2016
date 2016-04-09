# -*- coding: utf-8 -*-

import random
import math

RESULTADOS = range(2, 13)

def beta():
    lanzamientos = 0 # Lanzamientos necesarios
    
    while True:
        dado1 = random.randint(1, 6) # Dado 1
        dado2 = random.randint(1, 6) # Dado 2

        suma_dados = dado1 + dado2
        lanzamientos += 1

        if suma_dados in RESULTADOS:
            RESULTADOS.remove(suma_dados)

        if len(RESULTADOS) == 0:
            break

    return lanzamientos


def ejercicio03(n):
    lanzamientos = 0 # Lanzamientos necesarios
    
    for _ in xrange(n):
        while True:
            dado1 = random.randint(1, 6) # Dado 1
            dado2 = random.randint(1, 6) # Dado 2

            suma_dados = dado1 + dado2
            lanzamientos += 1

            if suma_dados in RESULTADOS:
                RESULTADOS.remove(suma_dados)

            if len(RESULTADOS) == 0:
                break

    return lanzamientos/float(n)


for n in [100, 1000, 10000, 100000]:
    print "n =", n, "--> Promedio =", ejercicio03(100)
