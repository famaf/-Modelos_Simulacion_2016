# -*- coding: utf-8 -*-

import random
import math


def esperanza(n):
    """
    Calcula la esperanza con la Ley de los Grandes Numeros.
    """
    N = 0 # Total de lanzamientos en los n experimentos

    for _ in xrange(n):
        RESULTADOS = range(2, 13) # Lista de resultados [2...12]
        lanzamientos = 0 # Lanzamientos necesarios

        # Mientras no se hayan obtenido todos los resultados tirar los dados
        while len(RESULTADOS) != 0:
            dado1 = random.randint(1, 6) # Dado 1
            dado2 = random.randint(1, 6) # Dado 2

            suma_dados = dado1 + dado2
            lanzamientos += 1

            # Si la suma de los dados esta en los resultados posibles
            # remover dicho resultado de los posibles (xq ya se obtuvo)
            if suma_dados in RESULTADOS:
                RESULTADOS.remove(suma_dados)

        N += lanzamientos

    return float(N)/n


def varianza(n):
    """
    Calcula la varianza en base a la esperanza.
    """
    N1 = 0
    N2 = 0

    for _ in xrange(n):
        RESULTADOS = range(2, 13) # Lista de resultados [2...12]
        lanzamientos = 0 # Lanzamientos necesarios

        # Mientras no se hayan obtenido todos los resultados tirar los dados
        while len(RESULTADOS) != 0:
            dado1 = random.randint(1, 6) # Dado 1
            dado2 = random.randint(1, 6) # Dado 2

            suma_dados = dado1 + dado2
            lanzamientos += 1

            # Si la suma de los dados esta en los resultados posibles
            # remover dicho resultado de los posibles (xq ya se obtuvo)
            if suma_dados in RESULTADOS:
                RESULTADOS.remove(suma_dados)

        N1 += lanzamientos # x
        N2 += lanzamientos**2 # x^2

    varianza = N2/float(n) - (N1/float(n))**2 # V(x) = E(x^2) - E(x)^2

    return varianza


for n in [100, 1000, 10000, 100000]:
    print("n =", n, "--> E(X) =", esperanza(n))

print("--------------------------------")

for n in [100, 1000, 10000, 100000]:
    print("n =", n, "--> V(X) =", varianza(n))
