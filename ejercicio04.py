# -*- coding: utf-8 -*-

import random
import math


def ejercicio04a(n):
    """
    Ejercicio 4a del Practico 3.
    """
    a = 0 # Acumulador de la suma de n tq' min{ n : Sn > 1 }
    for i in xrange(n):
        N = 2 # Es el n tq' min{ n : Sn > 1 } el min n que lo cumple es 2
        s = random.random() + random.random()

        # Si s es menor a 1 => sumamos un nuevo numero aleatorio y
        # actualizamos el n tq' min{ n : Sn > 1 }
        while s <= 1.0:
            s += random.random()
            N += 1

        a += N

    return float(a)/n


L = [100, 1000, 10000, 100000, 1000000]

for n in L:
    print "e =", ejercicio04a(n)
