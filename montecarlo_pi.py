# -*- coding: utf-8 -*-

import random
from math import sqrt

def montecarlo(n):
    """
    Calcula y devuelve el valor aproximado de pi usando el
    metodo de Montecarlo a partir de 'n' puntos.
    """
    g = 0
    for i in range(n):
        x = random.random()
        y = random.random()
        d = sqrt(x**2 + y**2)

        if d < 1:
            g += 1
    return 4*g/float(n)


n = int(raw_input("Ingrese la cantidad de puntos: "))

print "Pi =", montecarlo(n)
