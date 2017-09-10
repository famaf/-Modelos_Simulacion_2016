# -*- coding: utf-8 -*-

import random
import math


def generarPI(n):
    """
    Calcula y devuelve el valor aproximado de PI usando el
    metodo de Monte Carlo a partir de 'n' puntos.
    """
    PI = 0
    for _ in xrange(n):
        U = random.random() # U ~ U(0, 1)
        V = random.random() # V ~ U(0, 1)
        X = 2*U - 1 # X ~ U(-1, 1)
        Y = 2*V - 1 # Y ~ U(-1, 1)

        # Punto cae adentro del circulo de radio 1
        if X**2 + Y**2 <= 1:
            PI += 1

    PI = 4 * PI/float(n) # PI = 4 * PI/4

    return PI


n = int(raw_input("Ingrese la cantidad de puntos: "))


print("Pi =", generarPI(n))
