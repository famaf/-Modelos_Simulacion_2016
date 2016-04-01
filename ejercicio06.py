# -*- coding: utf-8 -*-

import random
import math

PI = math.pi

def buffon(n):
    """
    Ejercicio 6 del Practico 3.
    Simulacion del metodo: La Aguja de Buffon.
    """
    interseccion = 0
    for _ in xrange(n):
        r = random.uniform(0, 2)
        theta = random.uniform(0, PI)

        if r != 0.5 or r != 1.5:
            ya = r + 0.5*math.sin(theta)
            yb = r - 0.5*math.sin(theta)

            if yb <= 0 or ya >= 2:
                interseccion += 1

    return float(n)/interseccion

for n in [1000, 10000, 100000]:
    print "Pi =", buffon(n)
